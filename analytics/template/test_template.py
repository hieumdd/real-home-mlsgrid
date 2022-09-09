import pytest

from analytics.template import routes


@pytest.mark.parametrize(
    "options",
    [
        {
            "level": "day",
            "start": "2022-01-01",
            "end": "2022-01-01",
            "country": ["Country"],
        },
        {
            "level": "week",
            "by": "bedrooms_total",
            "country": ["Country"],
            "city": ["City"],
            "start": "2022-01-01",
            "end": "2022-01-01",
        },
    ],
)
@pytest.mark.parametrize(
    "template",
    [i for j in [x.values() for x in routes.values()] for i in j],
    ids=[i for j in [x.keys() for x in routes.values()] for i in j],
)
def test_template_render(options, template):
    res = template.render(options)
    print(res)
    res
