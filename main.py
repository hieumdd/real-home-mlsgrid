from typing import Any

from mlsgrid import mlsgrid_service
from mlsgrid.pipeline import pipelines


def main(request):
    data: dict[str, Any] = request.get_json()
    print(data)

    if "tasks" in data:
        response = mlsgrid_service.create_tasks_service()
    elif "table" in data:
        response = mlsgrid_service.pipeline_service(pipelines[data["table"]])
    else:
        raise ValueError(data)

    print(response)
    return response
