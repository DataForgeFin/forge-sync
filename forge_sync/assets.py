
import os
import requests

from dagster import asset, Output, AssetMaterialization


@asset
def get_cdi_data(context):
    response = requests.get(f"https://api.hgbrasil.com/finance/taxes?key={os.environ['API_KEY']}")
    context.log.info(f"Found {response.json()}")

    yield AssetMaterialization(asset_key="CDI_DATA", description="Data from HG API that has SELIC and CDI")
    yield Output(response)
