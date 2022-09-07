from datetime import datetime

from compose import compose

from db import bigquery
from mlsgrid import repo

TABLE = "Property"


def transform(rows: list[dict]) -> list[dict]:
    return [
        {
            "id": row.get("@odata.id"),
            "ListingId": row.get("ListingId"),
            "ListingKey": row.get("ListingKey"),
            "ModificationTimestamp": row.get("ModificationTimestamp"),
            "BedroomsTotal": row.get("BedroomsTotal"),
            "City": row.get("City"),
            "CloseDate": row.get("CloseDate"),
            "ClosePrice": row.get("ClosePrice"),
            "ContingentDate": row.get("ContingentDate"),
            "Country": row.get("Country"),
            "ListPrice": row.get("ListPrice"),
            "MajorChangeTimestamp": row.get("MajorChangeTimestamp"),
            "MajorChangeType": row.get("MajorChangeType"),
            "MlsStatus": row.get("MlsStatus"),
            "OffMarketDate": row.get("OffMarketDate"),
            "OnMarketDate": row.get("OnMarketDate"),
            "OriginalListPrice": row.get("OriginalListPrice"),
            "PostalCode": row.get("PostalCode"),
            "PreviousListPrice": row.get("PreviousListPrice"),
            "PropertySubType": row.get("PropertySubType"),
            "PropertyType": row.get("PropertyType"),
        }
        for row in rows
    ]


load = bigquery.load(
    TABLE,
    [
        {"name": "id", "type": "STRING"},
        {"name": "ListingId", "type": "STRING"},
        {"name": "ListingKey", "type": "STRING"},
        {"name": "ModificationTimestamp", "type": "TIMESTAMP"},
        {"name": "BedroomsTotal", "type": "NUMERIC"},
        {"name": "City", "type": "STRING"},
        {"name": "CloseDate", "type": "DATE"},
        {"name": "ClosePrice", "type": "NUMERIC"},
        {"name": "ContingentDate", "type": "DATE"},
        {"name": "Country", "type": "STRING"},
        {"name": "ListPrice", "type": "NUMERIC"},
        {"name": "MajorChangeTimestamp", "type": "TIMESTAMP"},
        {"name": "MajorChangeType", "type": "STRING"},
        {"name": "MlsStatus", "type": "STRING"},
        {"name": "OffMarketDate", "type": "DATE"},
        {"name": "OnMarketDate", "type": "DATE"},
        {"name": "OriginalListPrice", "type": "NUMERIC"},
        {"name": "PostalCode", "type": "STRING"},
        {"name": "PreviousListPrice", "type": "NUMERIC"},
        {"name": "PropertySubType", "type": "STRING"},
        {"name": "PropertyType", "type": "STRING"},
    ],
)


def pipeline_service(start: str, end: str) -> int:
    _start = (
        datetime.strptime(start, "%Y-%m-%d") if start else bigquery.get_latest(TABLE)
    )

    _end = datetime.strptime(end, "%Y-%m-%d") if end else datetime.utcnow()

    return compose(
        load,
        transform,
        repo.get_property,
    )((_start, _end))
