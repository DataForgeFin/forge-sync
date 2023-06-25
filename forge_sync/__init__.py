from dagster import Definitions, load_assets_from_modules

from . import assets
from .resources import MongoIO
import os

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    resources={
        "io_manager": MongoIO(
            database="forge_sync",
            collection="finance_metrics_low"
        ),
    },
)
