''' Connect Python to Mongo '''

import pymongo
from pymongo import MongoClient
import pprint


# default name
NAME_OF_DB = "test"

def init():
    ''' Initializes the mongo client'''
    # with full URI
    client = MongoClient('mongodb://localhost:27017/')
    db = client[NAME_OF_DB]
    return db

def getOneDoc(db_obj):
    ''' Get a collection and query a document'''
    all_collections = db_obj.collection_names(include_system_collections=False)
    print(all_collections)
    restaurants = db_obj.restaurants
    pprint.pprint(restaurants.find_one())

def getDetails(db_obj):
    ''' Gets all docs and stores them in a dict'''
    rest = []
    restaurants = db_obj.restaurants
    for doc in restaurants.find():
        rest.append(doc)

    print(rest)

def main():
    db_obj = init()
    # getOneDoc(db_obj)
    getDetails(db_obj)

if __name__ == '__main__':
    main()
