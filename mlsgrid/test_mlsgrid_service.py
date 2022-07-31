import pytest

from mlsgrid.pipeline import pipelines
from mlsgrid import mlsgrid_service

TIMEFRAME = [
    ("auto", None),
    ("manual", "2022-07-30"),
]

@pytest.fixture(
    params=[i[1] for i in TIMEFRAME],
    ids=[i[0] for i in TIMEFRAME],
)
def timeframe(request):
    return request.param


class TestMLSGrid:
    @pytest.fixture(
        params=pipelines.values(),
        ids=pipelines.keys(),
    )
    def pipeline(self, request):
        return request.param

    def test_service(self, pipeline, timeframe):
        res = mlsgrid_service.pipeline_service(pipeline, timeframe)
        assert res >= 0


class TestTasks:
    def test_service(self):
        res = mlsgrid_service.create_tasks_service()
        assert res["tasks"] > 0
