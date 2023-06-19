import os
from typing import Dict

import pymongo
from dagster import ConfigurableResource, Definitions


mongo_client = pymongo.MongoClient(os.getenv("MONGO_URI"))


class MongoDBResource(ConfigurableResource):
    database: str
    collection: str

    def write(self, json_data: Dict[str, str]):
        """Writes dict to the database collection"""
        connected_database = getattr(mongo_client, self.database)
        connected_collection = getattr(connected_database, self.collection)

        connected_collection.insert_one(json_data)
