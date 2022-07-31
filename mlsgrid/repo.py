import os
from datetime import datetime
import urllib

import httpx

TOP = 5000


def _get_client() -> httpx.Client:
    return httpx.Client(
        base_url="https://api.mlsgrid.com/v2",
        headers={"Authorization": f"Bearer {os.getenv('MLSGRID_TOKEN', '')}"},
        timeout=None,
    )


def get(resource: str):
    def _get(timeframe: datetime):
        def __get(client: httpx.Client, skip: int = 0):
            filter_ = f"OriginatingSystemName eq 'realtrac' and ModificationTimestamp gt {timeframe.isoformat(timespec='seconds')}.000Z"
            query = {
                "$filter": filter_,
                "$top": TOP,
                "$skip": skip,
            }
            qs = "&".join(
                [f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in query.items()]
            )

            r = client.get(f"{resource}?{qs}")
            res = r.json()

            data = res["value"]
            return data if not data else __get(client, skip + TOP)

        with _get_client() as client:
            return __get(client)

    return _get
