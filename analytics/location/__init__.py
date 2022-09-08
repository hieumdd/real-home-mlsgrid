from pathlib import PurePath

from analytics.template_service import query

current_page_name = PurePath(__file__).parent.name

median_average_house_price = query(f"{current_page_name}/median_average_house_price.sql.j2")

sales_price_vs_list_price_ratio = query(f"{current_page_name}/sales_price_vs_list_price_ratio.sql.j2")

inventory_by_type = query(f"{current_page_name}/inventory_by_type.sql.j2")

major_metrics = query(f"{current_page_name}/major_metrics.sql.j2")

inventory = query(f"{current_page_name}/inventory.sql.j2")
