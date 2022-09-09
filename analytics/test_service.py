import pytest

from analytics.template import routes
from analytics import service


@pytest.mark.parametrize(
    "options",
    [
        {
            "level": "day",
            "start": "2022-07-01",
            "end": "2022-08-01",
        },
        {
            "level": "week",
            "by": "bedrooms_total",
            "start": "2022-07-01",
            "end": "2022-08-01",
        },
    ],
)
@pytest.mark.parametrize(
    "template",
    [i for j in [x.values() for x in routes.values()] for i in j],
    ids=[i for j in [x.keys() for x in routes.values()] for i in j],
)
def test_template_render(options, template):
    res = service.analytics_service(options, template)
    print(res)
    res
