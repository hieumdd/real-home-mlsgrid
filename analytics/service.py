from typing import Any, Optional
from decimal import Decimal
from datetime import date

from jinja2 import Template

from db import bigquery


def parse_array(value: Optional[str]) -> list[str]:
    return value.split(",") if value else []


def serialize_value(value: Any) -> Any:
    if isinstance(value, date):
        return value.isoformat()
    elif isinstance(value, Decimal):
        return float(value)
    else:
        return value


def analytics_service(args: dict, template: Template):
    options = {
        "level": args.get("level"),
        "by": args.get("by"),
        "start": args.get("start"),
        "end": args.get("end"),
        "country": parse_array(args.get("country")),
        "city": parse_array(args.get("city")),
    }

    sql = template.render(options)

    data = [
        {k: serialize_value(v) for k, v in row.items()}
        for row in bigquery.get_client().query(sql).result()
    ]

    return {"data": data}
