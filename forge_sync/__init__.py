from dagster import Definitions, load_assets_from_modules

from . import assets, jobs
from .resources import MongoIO
import os

all_assets = load_assets_from_modules([assets], group_name="default")

defs = Definitions(
    assets=all_assets,
    resources={
        "io_manager": MongoIO(
            database="forge_sync",
            collection="finance_metrics_daily"
        ),
    },
    schedules=[jobs.default_schedule]
)
