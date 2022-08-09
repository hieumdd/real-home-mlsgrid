from datetime import datetime

from compose import compose

from db import bigquery
from tasks import cloud_tasks
from mlsgrid.pipeline.interface import Pipeline
from mlsgrid.pipeline import pipelines
from mlsgrid.repo import get


def pipeline_service(pipeline: Pipeline, start: str) -> int:
    _start = (
        datetime.strptime(start, "%Y-%m-%d")
        if start
        else bigquery.get_latest(pipeline.name)
    )

    return compose(
        bigquery.load(pipeline.name, pipeline.schema),
        pipeline.transform,
        get(pipeline.resource, pipeline.select),
    )(_start)


def create_tasks_service() -> dict[str, int]:
    return {
        "tasks": cloud_tasks.create_tasks(
            "mlsgrid",
            [{"table": table} for table in pipelines.keys()],
            lambda x: x["table"],
        )
    }
