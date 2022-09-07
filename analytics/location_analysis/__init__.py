from pathlib import PurePath

from analytics.templates import multi_level_query, single_level_query

current_page_name = PurePath(__file__).parent.name

median_average_house_price = multi_level_query(
    current_page_name,
    "median_average_house_price",
)

sales_price_vs_original_price_ratio = multi_level_query(
    current_page_name,
    "sales_price_vs_original_price_ratio",
)

inventory_by_type_big = multi_level_query(
    current_page_name,
    "inventory_by_type_big",
)

major_metrics = single_level_query(
    current_page_name,
    "major_metrics",
)

inventory_by_number_of_bedrooms = single_level_query(
    current_page_name,
    "inventory_by_number_of_bedrooms",
)

inventory_by_postcode = single_level_query(
    current_page_name,
    "inventory_by_postcode",
)

inventory_by_type = single_level_query(
    current_page_name,
    "inventory_by_type",
)
