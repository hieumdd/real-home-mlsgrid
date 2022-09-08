import pytest

from analytics.template import routes
from analytics import service


@pytest.mark.parametrize(
    "options",
    [
        {
            "level": "day",
            "start": "2022-01-01",
            "end": "2022-01-01",
            "country": "Country",
        },
        {
            "level": "week",
            "by": "bedrooms_total",
            "country": "Country, City",
            "city": "City",
            "start": "2022-01-01",
            "end": "2022-01-01",
        },
    ],
)
@pytest.mark.parametrize("template", routes.values(), ids=routes.keys())
def test_template_render(options, template):
    res = service.analytics_service(options, template)
    print(res)
    res
