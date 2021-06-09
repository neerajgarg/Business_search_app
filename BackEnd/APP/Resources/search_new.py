from flask_restful import Resource, reqparse

# User-Defined Modules
from APP import Mongodb
from APP.Resources import projection

class Search(Resource):

    # Argument Parser
    def _arguments(self, args: dict):
        filters = list()
        # Country filter
        if len(args.get('Country')) != 0:
            filters.append({'Country': {'$in': args.get('Country')}})
        # State/Region filter
        if args.get('State/Region'):
            filters.append({'State/Region': {'$in': args.get('State/Region')}})
        # City filter
        if args.get('City'):
            filters.append({'City': {'$in': args.get('City')}})
        # Text Search Parameter
        if args.get('job_title'):
            filters.append({'JobTitle': {'$in': args.get('job_title')}})
        if args.get('category'):
            filters.append({'Industry': {'$in': args.get('category')}})
        return filters

    # Method : POST    
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(name='job_title', location='json', type=list, required=True)
        parser.add_argument(name='category', location='json', type=list, required=True)
        parser.add_argument(name='country', location='json', type=list, dest='Country')
        parser.add_argument(name='state', location='json', type=list, dest='State/Region')
        parser.add_argument(name='city', location='json', type=list, dest='City')
        parser.add_argument(name='employee', location='json', type=str)
        parser.add_argument(name='limit', location='args', type=int, required=True)
        parser.add_argument(name='page', location='args', type=int, required=True)
        args = parser.parse_args(strict=True)
        try:
            filters = self._arguments(args=args)
            rows = args.get('limit')
            page = args.get('page')
            pipeline = [
                {'$match': {'$or': filters}},
                {'$skip': rows*(page-1) if page > 0 else 0},
                {'$limit': args.get('limit', 20)},
                {'$project': projection}
            ]
            # Update Keyword Collection for every Search
            response = Mongodb.Aggregation(
                pipeline = pipeline
            )
            output = list(response)
            result = dict()
            result['status'] = 'sucess'
            result['data'] = output
            result['count'] = len(output)
            return result, 200
        except Exception as e:
            result = dict()
            result['status'] = 'failure'
            result['message'] = 'InternalError'
            result['description'] = str(e)
            return result, 500