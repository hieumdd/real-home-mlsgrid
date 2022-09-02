import pytest

from mlsgrid import service


@pytest.mark.parametrize(
    ["start", "end"],
    [
        (None, None),
        ("2022-07-01", "2022-09-02"),
    ],
    ids=["auto", "manual"],
)
def test_pipeline_service(start, end):
    res = service.pipeline_service(start, end)
    assert res >= 0
