from analytics.location_analysis import median_average_house_price
from analytics.price_reduction import price_reduction


def test_query():
    options = {
        "level": "week",
        "by": "bedrooms_total",
        "country": ["sky"],
        "start": "2022-01-01",
        "end": "2022-01-01",
    }
    res = price_reduction(options)
    print(res)
    res
