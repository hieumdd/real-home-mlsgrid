from pathlib import PurePath

from analytics.template_service import query

current_page_name = PurePath(__file__).parent.name

price_reduction = query(f"{current_page_name}/price_reduction.sql.j2")
