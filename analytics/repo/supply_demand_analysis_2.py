from pypika import functions as fn

from analytics.repo.common import QueryOptions, Property, base_query, get_date_dimension
from analytics.repo.custom_fns import DATE_DIFF
from analytics.repo import filters


def metric_avg_days_on_market():
    return fn.Avg(DATE_DIFF(Property.CloseDate, Property.OnMarketDate, "DAY") + 1).as_(
        "avg_days_on_market"
    )


def days_on_market(options: QueryOptions):
    date_dimension, date_dimension_as = get_date_dimension(options["level"])

    q = (
        base_query(options)
        .where(filters.close_date(options))
        .groupby(date_dimension)
        .select(
            date_dimension.as_(date_dimension_as),
            metric_avg_days_on_market(),
        )
    )

    return q


def days_on_market_by_number_of_bedrooms(options: QueryOptions):
    date_dimension, date_dimension_as = get_date_dimension(options["level"])

    q = (
        base_query(options)
        .where(filters.close_date(options))
        .groupby(
            date_dimension,
            Property.BedroomsTotal,
        )
        .select(
            date_dimension.as_(date_dimension_as),
            Property.BedroomsTotal.as_("bedrooms_total"),
            metric_avg_days_on_market(),
        )
    )

    return q


def days_on_market_by_type(options: QueryOptions):
    date_dimension, date_dimension_as = get_date_dimension(options["level"])

    q = (
        base_query(options)
        .where(filters.close_date(options))
        .groupby(
            date_dimension,
            Property.PropertySubType,
        )
        .select(
            date_dimension.as_(date_dimension_as),
            Property.PropertySubType.as_("property_sub_type"),
            metric_avg_days_on_market(),
        )
    )

    return q


def under_contract_vs_closed_sales(options: QueryOptions):
    pass


def under_contract_vs_closed_sales_by_number_of_bedrooms(options: QueryOptions):
    pass


def under_contract_vs_closed_sales_by_type(options: QueryOptions):
    pass
