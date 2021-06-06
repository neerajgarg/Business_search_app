from os import name
from random import choices
from flask_restful import Resource, reqparse

# user-defined modules
from APP import Mongodb

class AutoComplete(Resource):

    def get(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(name='type', location='args', type=str, required=True, choices=('jobtitle', 'category'))
        parser.add_argument(name='keyword', location='args', type=str, required=True)
        args = parser.parse_args(strict=True)
        path = {
            'jobtitle': 'JobTitle',
            'category': 'Industry'
        }
        try:
            path = path.get(args.get('type'))
            pipeline = [
                {
                    '$search': {
                        'index': 'JobTitle_Autocomplete',
                        'autocomplete': {
                            'query': args.get('keyword'),
                            'path': path,
                            'tokenOrder': 'sequential'
                        }
                    }
                },
                {'$limit': 1000},
                {
                    '$group': {
                        '_id': f'${path}',
                        f'{path}': {'$addToSet': f'${path}'}
                    }
                },
                {
                    '$project': {
                        '_id': 1
                    }
                }
            ]
            response = Mongodb.Aggregation(
                pipeline = pipeline
            )
            output = list()
            for doc in response:
                output.append(doc.get('_id'))
            result = dict()
            result['status'] = 'success'
            result['data'] = output
            return result
        except Exception as e:
            result = dict()
            result['status'] = 'failure'
            result['message'] = 'Internal Error'
            result['description'] = str(e)
            return result, 500