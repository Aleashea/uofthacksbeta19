from pymongo import *


uri = 'mongodb://<hinamomori>:<hyacint5>@ds159574.mlab.com:59574/trashset'

client = MongoClient(uri)

db = client.get_database()

