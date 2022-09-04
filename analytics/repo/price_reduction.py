from pypika import functions as fn
from analytics.repo.common import QueryOptions, Property, base_query, get_date_dimension
from analytics.repo.custom_fns import DATE_DIFF
from analytics.repo import filters


def metric_avg_time_to_discount():
    return fn.Avg(
        DATE_DIFF(Property.CloseDate, fn.Date(Property.MajorChangeTimestamp), "DAY") + 1
    ).as_("avg_time_to_discount")


def avg_time_to_discount(options: QueryOptions):
    date_dimension, date_dimension_as = get_date_dimension(options["level"])

    q = (
        base_query(options)
        .where(
            filters.on_market_before_end(options)
            & filters.off_market_before_start(options)
        )
        .groupby(date_dimension)
        .select(
            date_dimension.as_(date_dimension_as),
            metric_avg_time_to_discount(),
        )
    )

    return q


def avg_time_to_discount_by_number_of_bedrooms(options: QueryOptions):
    date_dimension, date_dimension_as = get_date_dimension(options["level"])

    q = (
        base_query(options)
        .where(
            filters.on_market_before_end(options)
            & filters.off_market_before_start(options)
        )
        .groupby(date_dimension, Property.BedroomsTotal)
        .select(
            date_dimension.as_(date_dimension_as),
            Property.BedroomsTotal.as_("bedrooms_total"),
            metric_avg_time_to_discount(),
        )
    )

    return q


def avg_time_to_discount_by_type(options: QueryOptions):
    date_dimension, date_dimension_as = get_date_dimension(options["level"])

    q = (
        base_query(options)
        .where(
            filters.on_market_before_end(options)
            & filters.off_market_before_start(options)
        )
        .groupby(date_dimension, Property.PropertySubType)
        .select(
            date_dimension.as_(date_dimension_as),
            Property.PropertySubType.as_("property_sub_type"),
            metric_avg_time_to_discount(),
        )
    )

    return q


def avg_price_reduction(options: QueryOptions):
    pass


def avg_price_reduction_by_number_of_bedrooms(options: QueryOptions):
    pass


def avg_price_reduction_by_type(options: QueryOptions):
    pass
