
import os
import requests
from datetime import datetime

from dagster import asset, Output, AssetMaterialization, ResourceParam

from .resources import MongoDBResource


@asset
def get_cdi_data(context, db_conn: ResourceParam[MongoDBResource]):
    response = requests.get(f"https://api.hgbrasil.com/finance/taxes?key={os.environ['API_KEY']}")
    context.log.info(f"Found {response.json()}")
    json_data = response.json()
    parsed_data = {
        "date": datetime.strptime(json_data["results"][0]["date"], "%Y-%m-%d"),
        "metadata": {"metric": "selic"},
        "value": json_data["results"][0]["selic"],
    }
    db_conn.write(parsed_data)
    context.log.info("Document inserted into collection")
    yield AssetMaterialization(asset_key="CDI_DATA", description="Data from HG API that has SELIC and CDI")
    yield Output(
        value=response,
        metadata={"preview": response.text}
    )
