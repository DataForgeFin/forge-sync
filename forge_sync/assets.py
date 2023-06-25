
import os
import requests
from datetime import datetime
from typing import Dict, Any

from dagster import asset


@asset(description="Data from HG API that has SELIC")
def selic(context) -> Dict[str, Any]:
    response = requests.get(f"https://api.hgbrasil.com/finance/taxes?key={os.environ['API_KEY']}")
    context.log.info(f"Found {response.json()}")
    json_data = response.json()
    parsed_data = {
        "date": datetime.strptime(json_data["results"][0]["date"], "%Y-%m-%d"),
        "metadata": {"metric": "selic"},
        "value": json_data["results"][0]["selic"],
    }
    return parsed_data
