import pymongo
from pymongo import MongoClient
from os import environ

def getMongoClient():
    if environ.get('nasdaq_db') is None:
        raise Exception('Please set nasdaq_db connection value for mongodb.')
    return MongoClient(environ.get('nasdaq_db'))

def getMongoDB():
    return getMongoClient().get_database()

def getMongoCollection(collectionName):
    return getMongoDB()[collectionName]