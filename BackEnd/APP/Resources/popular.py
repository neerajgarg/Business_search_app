from flask_restful import reqparse, Resource

# User-defined Modules
from APP import Mongodb
from APP.Resources import projection

class Popular(Resource):

    def _scorecalculator(self, filters: list, score: int):
        pipeline = [
            {'$search': filters},
            {'$limit': 1},
            {'$project': {'score': {'$meta': 'searchScore'}}}
        ]
        max_score = list(Mongodb.Aggregation(pipeline))[0].get('score')
        addon_score = 75 - max_score
        return addon_score

    def get(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(name='search_type', location='args', type=str, required=True)
        parser.add_argument(name='keyword', location='args', type=str, required=True)
        args = parser.parse_args(strict=True)
        try:
            path = ['JobTitle', 'AssetName', 'CampaignName', 'CompanyName', 'Industry']
            if args.get('search_type') == 'job':
                path = 'JobTitle'
            query = {
                'index': 'Text_Search_Index',
                'text': {'path': path, 'query': args.get('keyword')}
            }
            addon_score = self._scorecalculator(filters=query, score=args.get('score', 100))
            pipeline = [
                {'$search': query},
                {'$project': projection},
                {'$skip': 0},
                {'$limit': args.get('limit', 20)}
            ]
            response = Mongodb.Aggregation(
                pipeline = pipeline
            )
            output = list()
            for i in response:
                i['score'] = int(i['score'] + addon_score)
                output.append(i)
            result = dict()
            result['status'] = 'sucess'
            result['data'] = output
            return result, 200
        except Exception as e:
            result = dict()
            result['status'] = 'failure'
            result['message'] = 'Internal Error'
            result['description'] = str(e)
            return result, 500