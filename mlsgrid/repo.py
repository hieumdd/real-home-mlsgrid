import os
from datetime import datetime
import urllib

import httpx

TOP = 5000

client = httpx.Client(
    base_url="https://api.mlsgrid.com/v2",
    headers={"Authorization": f"Bearer {os.getenv('MLSGRID_TOKEN', '')}"},
    timeout=None,
)


def get_property(timeframe: tuple[datetime, datetime]):
    start, end = [
        dt.replace(tzinfo=None).isoformat(timespec="milliseconds") + 'Z' for dt in timeframe
    ]

    filter_ = " and ".join(
        [
            "OriginatingSystemName eq 'realtrac'",
            f"ModificationTimestamp ge {start}",
            f"ModificationTimestamp le {end}",
        ]
    )

    select = ",".join(
        [
            "ListingId",
            "ListingKey",
            "ModificationTimestamp",
            "BedroomsTotal",
            "City",
            "CloseDate",
            "ClosePrice",
            "ContingentDate",
            "Country",
            "ListPrice",
            "MajorChangeTimestamp",
            "MajorChangeType",
            "MlsStatus",
            "OffMarketDate",
            "OnMarketDate",
            "OriginalListPrice",
            "PropertySubType",
            "PropertyType",
        ]
    )

    def _get(skip: int = 0):
        query = {"$filter": filter_, "$top": TOP, "$skip": skip, "$select": select}
        qs = "&".join(
            [f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in query.items()]
        )

        r = client.get(f"Property?{qs}")
        res = r.json()

        data = res["value"]
        return data if not data else data + _get(skip + TOP)

    return _get()
