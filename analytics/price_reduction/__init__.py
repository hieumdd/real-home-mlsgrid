from pathlib import PurePath

from analytics.templates import multi_level_query

current_page_name = PurePath(__file__).parent.name

avg_time_to_discount = multi_level_query(
    current_page_name,
    "avg_time_to_discount",
)

avg_time_to_discount_by_number_of_bedrooms = multi_level_query(
    current_page_name,
    "avg_time_to_discount_by_number_of_bedrooms",
)

avg_time_to_discount_by_type = multi_level_query(
    current_page_name,
    "avg_time_to_discount_by_type",
)
