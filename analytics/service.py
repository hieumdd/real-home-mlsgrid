from typing import Optional

from flask import Request
from jinja2 import Template

from db import bigquery


def parse_array(value: Optional[str]) -> list[str]:
    return value.split(",") if value else []


def analytics_service(request: Request, template: Template):
    args = request.args

    options = {
        "level": args.get("level"),
        "by": args.get("by"),
        "start": args.get("start"),
        "end": args.get("end"),
        "country": parse_array(args.get("country")),
        "city": parse_array(args.get("city")),
    }

    sql = template.render(options)

    data = [dict(i) for i in bigquery.get_client().query(sql).result()]

    return {"data": data}
