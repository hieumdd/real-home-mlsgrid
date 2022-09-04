from typing import Callable

from flask import Request
from pypika.queries import QueryBuilder

from db import bigquery
from analytics.repo.common import QueryOptions

Builder = Callable[[QueryOptions], QueryBuilder]


def analytics_service(
    builder: Callable[[QueryOptions], QueryBuilder],
    request: Request,
):
    body = request.get_json()

    if body:
        options: QueryOptions = {
            "level": body["level"],
            "start": body["start"],
            "end": body["end"],
            "country": body.get("country"),
            "city": body.get("city"),
        }

        sql = builder(options).get_sql()

        data = [dict(i) for i in bigquery.get_client().query(sql).result()]

        return {"data": data}
    else:
        raise ValueError
