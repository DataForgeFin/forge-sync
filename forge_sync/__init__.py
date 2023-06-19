from dagster import Definitions, load_assets_from_modules

from . import assets
from .resources import MongoDBResource

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    resources={"db_conn": MongoDBResource(database="forge_sync", collection="finance_metrics_low")},
)
