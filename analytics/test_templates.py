from analytics.location_analysis import median_average_house_price

def test_query():
    options = {
        "level": "day",
        "start": "2022-01-01",
        "end": "2022-01-01"
    }
    res = median_average_house_price(options)
    print(res)
    res
