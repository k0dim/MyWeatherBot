import pymongo
from datetime import datetime


class DBweather:
    def __init__(self):
        self.client = pymongo.MongoClient("localhost", 27017)
        self.db = self.client['weatherbotdb']
        self.collectins = self.db['location']

    def search_user(self, id):
        return self.collectins.find_one({'_id': id})
        

    def insert(self, id, username, latitude, longitude):
        post = {
            '_id': id,
            'username': f'@{username}',
            'latitude': latitude,
            'longitude': longitude,
            'datetime': str(datetime.now()),
        }
        return self.collectins.insert_one(post)

    def update(self, id, latitude, longitude):
        filters = {'_id': id}
        update = {"$set":
            {
            'latitude': latitude,
            'longitude': longitude,
            'datetime': str(datetime.now()),
            }
        }
        return self.collectins.update_one(filters, update)