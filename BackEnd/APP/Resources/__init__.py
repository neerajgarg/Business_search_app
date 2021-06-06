from flask_restful import Resource

projection = {
    '_id': {'$convert': {'input': '$_id', 'to': 'string'}},
    'address': {'$concat': ['$StreetAddress', ', ', {'$convert': {'input': '$City', 'to': 'string'}}, ' - ', {'$convert': {'input': '$PostalCode', 'to': 'string'}}, ', ', '$State/Region', ', ', '$Country']},
    'city': {'$convert': {'input': '$City', 'to': 'string'}},
    'country': {'$convert': {'input': '$Country', 'to': 'string'}},
    'campaign': '$CampaignName',
    'company_name': '$CompanyName',
    'email': '$Email',
    'employees': '$NumberOfEmployees',
    'first_name': '$FirstName',
    'industry': '$Industry',
    'job_level': '$JobLevel',
    'job_title': '$JobTitle',
    'last_name': '$LastName',
    'phone': '$PhoneNumber',
    'revenue': '$Revenue',
    'salutation': '$Salutation',
    'score': {'$meta': 'searchScore'},
    'tag_line': '$AssetName'
}

class Version(Resource):
    def get(self):
        result = dict()
        result['status'] = 'success'
        result['version'] = 'v1'
        result['description'] = 'DataInsight - DB API'
        return result, 200