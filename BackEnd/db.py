import re
from typing import Container
import pandas as pd
from pymongo import MongoClient

url = 'mongodb+srv://Api_Admin:DbApi_admin@cluster0.idnak.mongodb.net/?retryWrites=true&w=majority'
db_name = 'DataInsight_DB'
colls_name = 'Company_Details_Colls'

client = MongoClient(url)

database = client.get_database(name=db_name)

container = database.get_collection(name=colls_name)

pipeline = [
    {
        '$search': {
            'index': 'JobTitle_Autocomplete',
            'autocomplete': {
                'query': 'senior',
                'path': 'JobTitle',
                'tokenOrder': 'sequential'
            }
        }
    },
    {'$limit': 1000},
    {
        '$group': {
            '_id': '$JobTitle',
            'JobTitle': {'$addToSet': '$Jobtitle'}
        }
    },
    {
        '$project': {
            '_id': 1
        }
    }
]

docs = container.aggregate(pipeline=pipeline)
for doc in docs:
    print(doc)