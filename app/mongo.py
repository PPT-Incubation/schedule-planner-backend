from pymongo import MongoClient

from .settings import settings

try:
    client = MongoClient(settings.connection_string, serverSelectionTimeoutMS = 5000)
except Exception as e:
    print("Unable to connect to MongoDB")
    print(e)
