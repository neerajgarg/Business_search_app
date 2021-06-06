from pymongo import MongoClient, ASCENDING, DESCENDING

class MongoDB:
    def __init__(self, url, db_name, colls_name):
        self.client = MongoClient(url)
        self.db = self.client.get_database(name=db_name)
        self.container = self.db.get_collection(name=colls_name)
    
    def Aggregation(self, pipeline):
        response = self.container.aggregate(
            pipeline = pipeline,
            allowDiskUse = True
        )
        return response
    
    def Distinct(self, filters, key):
        response = self.container.distinct(
            key = key,
            filter = filters
        )
        return response
    
    def Query(self, filters, colls, projection):
        sort = [('qty', DESCENDING)]
        response = self.db.get_collection(colls).find(projection=projection).sort(sort).limit(5)
        return response
    
    def Insert(self, docs, colls):
        response = self.db.get_collection(colls).insert_one(docs)
        return response
    
    def Update(self, docs, colls, update):
        response = self.db.get_collection(name=colls).update_one(
            filter = docs,
            update = update,
            upsert = True
        )
        return response