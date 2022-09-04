from typing import TypedDict, Optional

from pypika import MySQLQuery, Table, functions as fns, analytics, CustomFunction, AnalyticFunction


class QueryOptions(TypedDict):
    level: str
    start: str
    end: str
    country: Optional[str]
    city: Optional[str]


Property = Table("Property")

DATE_TRUNC = CustomFunction("DATE_TRUNC", ["date_expression", "date_part"])
MEDIAN = lambda column: CustomFunction(
    "PERCENTILE_CONT",
    ["value_expression", "value"],
)(column, 0.5)

MEDIAN2 = AnalyticFunction("")


def base_query(options: QueryOptions):
    q = MySQLQuery.from_(Property)

    if options.get("country"):
        q = q.where(Property.Country == options["country"])

    if options.get("city"):
        q = q.where(Property.City == options["city"])

    return q


class LocationAnalysis:
    @staticmethod
    def median_average_house_price(options: QueryOptions):
        q = base_query(options).where(
            Property.CloseDate[options["start"] : options["end"]]  # type: ignore
        )

        if options["level"] == "week":
            week = DATE_TRUNC(Property.CloseDate, "WEEK")
            q = q.groupby(week).select(week.as_("date"))
        elif options["level"] == "month":
            month = DATE_TRUNC(Property.CloseDate, "MONTH")
            q = q.groupby(month).select(month.as_("date"))
        else:
            q = q.groupby(Property.CloseDate).select(Property.CloseDate.as_("date"))

        q = q.where(Property.MlsStatus == "Closed").select(
            fns.Avg(Property.ClosePrice).as_("avg_close_price"),
            fns.Avg(MEDIAN(Property.ClosePrice).as_("median_close_price")),
        )

        return q

    @staticmethod
    def sales_price_vs_original_price_ratio(options: QueryOptions):
        q = base_query(options).where(
            Property.CloseDate[options["start"] : options["end"]]  # type: ignore
        )

        if options["level"] == "week":
            week = DATE_TRUNC(Property.CloseDate, "WEEK")
            q = q.groupby(week).select(week.as_("date"))
        elif options["level"] == "month":
            month = DATE_TRUNC(Property.CloseDate, "MONTH")
            q = q.groupby(month).select(month.as_("date"))
        else:
            q = q.groupby(Property.CloseDate).select(Property.CloseDate.as_("date"))

        q = q.where(Property.MlsStatus == "Closed").select(
            (fns.Sum(Property.ClosePrice) / fns.Sum(Property.OriginalListPrice)).as_(
                "sales_price_ratio"
            ),
            (fns.Sum(Property.ClosePrice) / fns.Sum(Property.ListPrice)).as_(
                "list_price_ratio"
            ),
        )

        return q

    @staticmethod
    def inventory_by_type(options):
        q = base_query(options).where(
            (Property.OnMarketDate <= options["end"])
            & (
                (Property.OffMarketDate >= options["start"])
                | (Property.ContigentDate >= options["start"])
            )
        )

        if options["level"] == "week":
            week = DATE_TRUNC(Property.CloseDate, "WEEK")
            q = q.groupby(week).select(week.as_("date"))
        elif options["level"] == "month":
            month = DATE_TRUNC(Property.CloseDate, "MONTH")
            q = q.groupby(month).select(month.as_("date"))
        else:
            q = q.groupby(Property.CloseDate).select(Property.CloseDate.as_("date"))

        q = q.where(Property.MlsStatus == "Closed").select(
            Property.PropertyType.as_("property_type"),
            fns.Count(Property.ListingId).as_("count_inventory"),
        )

        return q

    @staticmethod
    def sales_price_vs_list_price_ratio(options):
        q = base_query(options).where(
            Property.CloseDate[options["start"] : options["end"]]  # type: ignore
        )

        if options["level"] == "week":
            week = DATE_TRUNC(Property.CloseDate, "WEEK")
            q = q.groupby(week).select(week.as_("date"))
        elif options["level"] == "month":
            month = DATE_TRUNC(Property.CloseDate, "MONTH")
            q = q.groupby(month).select(month.as_("date"))
        else:
            q = q.groupby(Property.CloseDate).select(Property.CloseDate.as_("date"))

        q = q.where(Property.MlsStatus == "Closed").select(
            fns.Avg(MEDIAN(Property.OriginalListPrice).as_("median_close_price")),
            fns.Avg(MEDIAN(Property.ClosePrice).as_("median_close_price")),
            Property.PropertyType.as_("property_type"),
            fns.Count(Property.ListingId).as_("count_inventory"),
        )

        return q
