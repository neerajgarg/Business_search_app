from flask_restful import Resource, reqparse
from bson.objectid import ObjectId

# User-Defined Modules
from APP import Mongodb
from APP.config import Config
from APP.Resources import projection

class Search(Resource):

    # Argument Parser
    def _arguments(self, args: dict):
        print(args)
        print()
        filters = list()
        match = list()
        # Country filter
        if len(args.get('Country')) != 0:
            filters.append({'text':{'path': 'Country', 'query':' OR '.join(args.get('Country'))}})

        
        # State/Region filter
        if args.get('State/Region') != None and args.get('State/Region') != "":
            filters.append({'text':{'path': 'State/Region', 'query':args.get('State/Region')}})


        # City filter
        if args.get('City') != None and args.get('City') != "":
            filters.append({'text':{'path': 'City', 'query':args.get('City')}})

        #Category filter
        if args.get('category') != None and args.get('category') != "":
            filters.append({'text':{'path': 'Industry', 'query':args.get('category')}})

        #jobtitle filter
        if args.get('jobtitle') != None and args.get('jobtitle') != "":
            filters.append({'text':{'path': 'JobTitle', 'query':args.get('jobtitle')}})

        # Text Search Parameter
        path = ['JobTitle', 'AssetName', 'CampaignName', 'CompanyName', 'Industry']
        if args.get('search_type') == 'job':
            path = 'JobTitle'
        
        if(args.get('keyword')!=""):
            filters.append({'text':{'path': path, 'query':args.get('keyword')}})
        print ("\nfilters : ",filters,"\n")
        print(match)
        return filters,match
    
    def _scorecalculator(self, filters: list, score: int):
        pipeline = [
            {'$search': filters},
            {'$limit': 1},
            {'$project': {'score': {'$meta': 'searchScore'}}}
        ]
        response = list(Mongodb.Aggregation(pipeline))
        if len(response) != 0:
            max_score = response[0].get('score')
            scoring = max_score * (score / 75)
            addon_score = 75 / max_score
            return scoring, addon_score
        return 75, 75
    
    def _updatekeyword(self, keyword):
        pass
    
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(name='category', location='json', type=str)
        parser.add_argument(name='jobtitle', location='json', type=str)
        parser.add_argument(name='search_type', location='json', type=str, required=True)
        parser.add_argument(name='keyword', location='json', type=str, required=True)
        parser.add_argument(name='country', location='json', type=list, dest='Country')
        parser.add_argument(name='state', location='json', type=str, dest='State/Region')
        parser.add_argument(name='city', location='json', type=str, dest='City')

        parser.add_argument(name='employee', location='json', type=str)
        parser.add_argument(name='score', location='json', type=int)

        #page and limit being retrived from the url post method
        parser.add_argument(name='limit', location='args', type=int, required=True)
        parser.add_argument(name='page', location='args', type=int, required=True)
        args = parser.parse_args(strict=True)
        try:
            filters,match = self._arguments(args=args)
            query = {
                'index': 'Text_Search_Index',
                'compound': {
                    'must': filters
                }
            }
            scoring, addon_score = self._scorecalculator(filters=query, score=args.get('score', 100))
            rows = args.get('limit')
            page = args.get('page')
            pipeline = [
                {'$search': query},
                {'$project': projection},
                # {'$match': {'employees': match}},    # not worth it takeing more than 2 minutes for backend filtering 
                {'$skip': rows*(page-1) if page > 0 else 0},
                {'$limit': args.get('limit', 20)},
                
            ]
            # Update Keyword Collection for every Search
            Mongodb.Update(
                colls = Config.KEYWORD_COLLS,
                docs = {'keyword': args.get('keyword').strip().capitalize()},
                update = {'$inc': {'qty': 1}}
            ) 
            
            response = Mongodb.Aggregation(
                pipeline = pipeline
            )
            output = list()
            for i in response:
                i['score'] = int(i['score'] * addon_score)
                output.append(i)
            result = dict()
            result['status'] = 'sucess'
            result['data'] = output
            result['count'] = len(output)
            return result, 200
        except Exception as e:
            result = dict()
            print ("\nError!!!\n",e)
            result['status'] = 'failure'
            result['message'] = 'InternalError'
            result['description'] = str(e)
            return result, 500