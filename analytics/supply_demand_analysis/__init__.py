from pathlib import PurePath

from analytics.templates import multi_level_query

current_page_name = PurePath(__file__).parent.name

days_on_market = multi_level_query(
    current_page_name,
    "days_on_market",
)

days_on_market_by_number_of_bedrooms = multi_level_query(
    current_page_name,
    "days_on_market_by_number_of_bedrooms",
)

days_on_market_by_type = multi_level_query(
    current_page_name,
    "days_on_market_by_type",
)
