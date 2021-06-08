from flask_restful import Resource, reqparse, inputs
import re
# User Defined Modules
from APP import Mongodb
from APP.config import Config

class State(Resource):
    def get(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(name='country', location='args', type=str, dest='Country')
        args = parser.parse_args(strict=True)
        try:
            filters = None
            if args.get('Country') != "" and args.get('Country') != None:
                filters = {'Country': args.get('Country')}
            response = Mongodb.db.get_collection(Config.COUNTRY_COLLS).distinct(
                key = 'State',
                filter = filters
            )
            result = dict()
            result['status'] = 'success'
            result['data'] = list(response)
            return result
        except Exception as e:
            result = dict()
            result['status'] = 'failure'
            result['message'] = 'Internal Error'
            result['description'] = str(e)
            return result, 500
    
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(name='country', location='json', type=list, dest='Country')
        args = parser.parse_args(strict=True)
        try:
            filters = None
            if len(args.get('Country')) != 0:
                filters = {'Country': {'$in': args.get('Country')}}
            response = Mongodb.db.get_collection(Config.COUNTRY_COLLS).distinct(
                key = 'State',
                filter = filters
            )
            result = dict()
            result['status'] = 'success'
            result['data'] = list(response)
            return result
        except Exception as e:
            result = dict()
            result['status'] = 'failure'
            result['message'] = 'Internal Error'
            result['description'] = str(e)
            return result, 500

class Cities(Resource):
    def get(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(name='country', location='args', type=str, dest='Country')
        parser.add_argument(name='state', location='args', type=str, dest='State')
        args = parser.parse_args(strict=True)
        try:
            filters = dict()
            if args.get('Country') != "" and args.get('Country') != None:
                filters['Country'] = args.get('Country')
            if args.get('State') != "" and args.get('State') != None:
                filters['State'] = args.get('State')
            response =Mongodb.db.get_collection(Config.COUNTRY_COLLS).distinct(
                key = 'City',
                filter = filters
            )
            result = dict()
            result['status'] = 'success'
            result['data'] = list(response)
            return result
        except Exception as e:
            result = dict()
            result['status'] = 'failure'
            result['message'] = 'Internal Error'
            result['description'] = str(e)
            return result, 500
class Category(Resource):
    def get(self):
        try: 
            response = Mongodb.db.get_collection(Config.COMPANY_COLLS_NAME).distinct(
                key = 'Industry'
            )
            result = dict()
            result['status'] = 'success'
            result['Categories'] = list(response)
            return result, 200
        except Exception as e:
            result = dict()
            result['status'] = 'failure'
            result['message'] = 'Internal Error'
            result['description'] = str(e)
            return result, 500

class JobTitle(Resource):
    def get(self):
        try: 
            # parser = reqparse.RequestParser()
            # parser.add_argument('query', type=str, location='args')
            # args = parser.parse_args(strict=True)
            response = Mongodb.db.get_collection(Config.COMPANY_COLLS_NAME).distinct(
                key = 'JobTitle',
                # { 'JobTitle': re.compile(args['query'], re.IGNORECASE)}
            )
            result = dict()
            result['status'] = 'success'
            result['Titles'] = list(response)
            print(len(result['Titles']))
            return result, 200
        except Exception as e:
            result = dict()
            result['status'] = 'failure'
            result['message'] = 'Internal Error'
            result['description'] = str(e)
            return result, 500

class Keywords(Resource):
    def get(self):
        try:
            projection = dict()
            projection['keyword'] = True
            projection['_id'] = False
            response = Mongodb.Query(filters = None, colls=Config.KEYWORD_COLLS, projection=projection)
            keywords = list()
            for i in response:
                keywords.append(i.get('keyword'))
            result = dict()
            result['status'] = 'success'
            result['data'] = keywords
            return result
        except Exception as e:
            result = dict()
            result['status'] = 'failure'
            result['message'] = 'Internal Error'
            result['description'] = str(e)
            return result, 500

class CountryGroups(Resource):
    def get(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(name='country_group', location='args', type=str, dest='GroupName')
        args = parser.parse_args(strict=True)
        try:
            response = Mongodb.db.get_collection(Config.COUNTRY_GROUP_COLLS).find_one(
                filter = {'GroupName': args.get('GroupName')}
            )
            result = dict()
            result['status'] = 'success'
            if response:
                result['GroupName'] = response.get('GroupName')
                result['Countries'] = response.get('Countries')
                return result, 200
            else:
                result['message'] = 'No Group Found'
                return result, 200
        except Exception as e:
            result = dict()
            result['status'] = 'failure'
            result['message'] = 'Internal Error'
            result['description'] = str(e)
            return result, 500

class ListGroups(Resource):
    def get(self):
        try:
            response = Mongodb.db.get_collection(Config.COUNTRY_GROUP_COLLS).distinct(
                key = 'GroupName'
            )
            result = dict()
            result['status'] = 'success'
            result['data'] = list(response)
            return result, 200
        except Exception as e:
            result = dict()
            result['status'] = 'failure'
            result['message'] = 'Internal Error'
            result['description'] = str(e)
            return result, 500


class Country(Resource):
    def get(self):
        try:
            response = Mongodb.db.get_collection(Config.COUNTRY_COLLS).distinct(
                key = 'Country'
            )
            result = dict()
            result['status'] = 'success'
            result['data'] = list(response)
            return result, 200
        except Exception as e:
            result = dict()
            result['status'] = 'failure'
            result['message'] = 'Internal Error'
            result['description'] = str(e)
            return result, 500
