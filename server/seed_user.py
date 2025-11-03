from db import MongoDB
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from passwords import mongodb_uri

client = MongoClient(mongodb_uri, server_api=ServerApi('1'))
db = MongoDB(client)

user_id = "testuser"
db.add_user(user_id)