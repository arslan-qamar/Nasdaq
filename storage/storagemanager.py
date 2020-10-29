from mongohelper import *
from datetime import datetime
from pymongo import UpdateOne

COLLECTION_NAME = 'listings'

def storeData(data):
    collection = getMongoCollection(COLLECTION_NAME)

    ops = []
    for d in data:
        filter = {
            '_id': d['ticker']
            }
            
        upsert_data = d      

        ops.append(UpdateOne(filter,
            {
                "$set": upsert_data,
                "$setOnInsert": { "Discovered_At": datetime.utcnow() }
            },
            True))

        print(upsert_data)        
    
    collection.bulk_write(ops)
        
def getNewListings(startDate):
    collection = getMongoCollection(COLLECTION_NAME)

    results = collection.find({'Discovered_At' : {'$gte' : startDate}})
    return results
