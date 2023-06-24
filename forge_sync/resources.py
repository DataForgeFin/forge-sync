import os

import pymongo
from dagster import ConfigurableIOManager


MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")


class MongoIO(ConfigurableIOManager):
    database: str
    collection: str

    def handle_output(self, context, obj):
        context.log.info(f"Saving results")
        client = pymongo.MongoClient(MONGO_URI)
        db = client[self.database]
        collection = db[self.collection]
        collection.insert_one(obj)
        client.close()

    def load_input(self, context):
        context.log.error(f"Not implemented load from MongoDB")
        raise NotImplementedError()
