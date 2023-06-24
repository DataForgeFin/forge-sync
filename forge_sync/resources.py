import os
from typing import Dict

import pymongo
from dagster import ConfigurableIOManager


class MongoIO(ConfigurableIOManager):
    connection_string: str
    database: str
    collection: str

    def handle_output(self, context, obj):
        context.log.info(f"Saving results")
        client = pymongo.MongoClient()
        db = client[self.database]
        collection = db[self.collection]
        collection.insert_one(obj)
        client.close()

    def load_input(self, context):
        context.log.error(f"Not implemented load from MongoDB")
        raise NotImplementedError()
