from pymongo import *


uri = 'mongodb://user:pass@host:port/db'

client = MongoClient(uri)

db = client.get_database()

