
import os
import requests
from datetime import datetime
from typing import Dict, Any

from dagster import asset


def parse_hg_taxes(response, metric):
    parsed_data = {
        "date": datetime.strptime(response["date"], "%Y-%m-%d"),
        "metric": metric,
        "value": response[metric],
        "metadata": {"execution_at": datetime.now()},
    }
    return parsed_data

@asset(description="Data from HG that has SELIC and CDI")
def hg_taxes(context) -> Dict:
    response = requests.get(f"https://api.hgbrasil.com/finance/taxes?key={os.environ['API_KEY']}").json()
    context.log.info(f"Found {response}")
    return response['results'][0]


@asset(io_manager_key="mongo_io")
def selic(context, hg_taxes) -> Dict[str, Any]:
    context.log.info(f"Starting to parse")
    parsed_data = parse_hg_taxes(hg_taxes, "selic")
    context.log.info(f"Parsing result %s", parsed_data)
    return parsed_data


@asset(io_manager_key="mongo_io")
def cdi(context, hg_taxes) -> Dict[str, Any]:
    context.log.info(f"Starting to parse")
    parsed_data = parse_hg_taxes(hg_taxes, "cdi")
    context.log.info(f"Parsing result %s", parsed_data)
    return parsed_data
