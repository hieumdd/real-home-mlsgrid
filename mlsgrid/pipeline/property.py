from mlsgrid.pipeline.interface import Pipeline

pipeline = Pipeline(
    name="Property",
    resource="Property",
    select=",".join(
        [
            "ListingId",
            "ListingKey",
            "CloseDate",
            "ClosePrice",
            "ModificationTimestamp",
        ]
    ),
    transform=lambda rows: [
        {
            "id": row.get("@odata.id"),
            "ListingId": row.get("ListingId"),
            "ListingKey": row.get("ListingKey"),
            "CloseDate": row.get("CloseDate"),
            "ClosePrice": row.get("ClosePrice"),
            "ModificationTimestamp": row.get("ModificationTimestamp"),
        }
        for row in rows
    ],
    schema=[
        {"name": "id", "type": "STRING"},
        {"name": "ListingId", "type": "STRING"},
        {"name": "ListingKey", "type": "STRING"},
        {"name": "CloseDate", "type": "DATE"},
        {"name": "ClosePrice", "type": "NUMERIC"},
        {"name": "ModificationTimestamp", "type": "TIMESTAMP"},
    ],
)
