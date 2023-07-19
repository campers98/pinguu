from sys import exit

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pymongo import MongoClient
from pymongo.errors import PyMongoError

from AsuX import LOGGER
from config import MONGO_DB_URL

DB_NAME = "AsuX"

try:
    _client = MongoClient(MONGO_DB_URL)
except PyMongoError as f:
    LOGGER.error(f"Error in Mongodb: {f}")
    exit(1)

# Pymongo Database
db = _client[DB_NAME]

# motor Database
mongo = MongoCli(MONGO_DB_URL)
mdb = mongo.AsuX_


class MongoDB:
    """Class for interacting with Bot database."""

    def __init__(self, collection) -> None:
        self.collection = db[collection]

    # Insert one entry into collection
    def insert_one(self, document):
        result = self.collection.insert_one(document)
        return repr(result.inserted_id)

    # Find one entry from collection
    def find_one(self, query):
        result = self.collection.find_one(query)
        if result:
            return result
        return False

    # Find entries from collection
    def find_all(self, query=None):
        if query is None:
            query = {}
        return list(self.collection.find(query))

    # Count entries from collection
    def count(self, query=None):
        if query is None:
            query = {}
        return self.collection.count_documents(query)

    # Delete entry/entries from collection
    def delete_one(self, query):
        self.collection.delete_many(query)
        return self.collection.count_documents({})

    # Replace one entry in collection
    def replace(self, query, new_data):
        old = self.collection.find_one(query)
        _id = old["_id"]
        self.collection.replace_one({"_id": _id}, new_data)
        new = self.collection.find_one({"_id": _id})
        return old, new

    # Update one entry from collection
    def update(self, query, update):
        result = self.collection.update_one(query, {"$set": update})
        new_document = self.collection.find_one(query)
        return result.modified_count, new_document

    @staticmethod
    def close():
        return _client.close()


def __connect_first():
    _ = MongoDB("test")
    LOGGER.info("Initialized Database!\n")


__connect_first()
