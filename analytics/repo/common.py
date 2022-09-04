from typing import TypedDict, Optional

from pypika import MySQLQuery, Table

from analytics.repo.custom_fns import DATE_TRUNC


class QueryOptions(TypedDict):
    level: str
    start: str
    end: str
    country: Optional[str]
    city: Optional[str]


Property = Table("Property")


def base_query(options: QueryOptions):
    q = MySQLQuery.from_(Property)

    if options.get("country"):
        q = q.where(Property.Country == options["country"])

    if options.get("city"):
        q = q.where(Property.City == options["city"])

    return q


def get_date_dimension(level):
    mapping = {
        "week": (DATE_TRUNC(Property.CloseDate, "WEEK"), "start_of_week"),
        "month": (DATE_TRUNC(Property.CloseDate, "MONTH"), "start_of_month"),
    }
    return mapping.get(
        level,
        (Property.CloseDate, "date"),
    )
