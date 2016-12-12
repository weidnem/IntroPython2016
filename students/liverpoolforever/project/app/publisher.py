''' Connect Python to Mongo '''

import pymongo
import pprint

from pymongo import MongoClient
from .formatter import Formatter


class Publisher():
    ''' A publisher to a MongoDB'''

    db_name = "test"
    host = "mongodb://localhost:27017/"

    def __init__(self,loc):
        ''' Gets a client and the database obj'''
        self.client = MongoClient(self.host)
        self.db_obj = self.client["test"]
        self.location = loc
        try:
            self.restaurants = self.db_obj.restaurants
            # pprint.pprint(self.restaurants.find_one())
        except:
            print("No collection named {}".format(self.collection))


    def __str__(self):
        return "A mongodb publisher object with host {} and url: {}".format(self.client,self.db_name)

    def __repr__(self):
        return "Publisher({})".format(self.host)

    @property
    @Formatter('aniceformat')
    def count_restaurants(self):
        ''' Counts restaurants in a location'''
        query_filter = dict(borough=self.location)
        count = self.restaurants.find(query_filter).count()
        return count

    def get_document(self):
     query_filter = dict(borough=self.location)
     for rest in self.restaurants.find(query_filter):
        pprint.pprint(rest)



# if __name__ == '__main__':
#     pub = Publisher('Brooklyn')
#     print(pub.count_restaurants)
    # print(pub.format_result())
    # print(pub.restaurant())
