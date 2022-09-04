from pypika import functions as fn
from analytics.repo.common import QueryOptions, Property, base_query, get_date_dimension
from analytics.repo import custom_fns, filters


def metric_median_close_price(over):
    return fn.Avg(
        custom_fns.MEDIAN(Property.ClosePrice).over(over).as_("median_close_price")
    )


def metric_median_original_list_price(over):
    return fn.Avg(
        custom_fns.MEDIAN(Property.OriginalListPrice)
        .over(over)
        .as_("median_original_list_price")
    )


def median_average_house_price(options: QueryOptions):
    date_dimension, date_dimension_as = get_date_dimension(options["level"])

    q = (
        base_query(options)
        .where(filters.close_date(options))
        .where(filters.mls_status_closed())
        .groupby(date_dimension)
        .select(
            date_dimension.as_(date_dimension_as),
            fn.Avg(Property.ClosePrice).as_("avg_close_price"),
            metric_median_close_price(date_dimension),
        )
    )

    return q


def sales_price_vs_original_price_ratio(options: QueryOptions):
    pass


def inventory_by_type(options):
    date_dimension, date_dimension_as = get_date_dimension(options["level"])

    q = (
        base_query(options)
        .where(filters.market_date(options))
        .where(filters.mls_status_closed())
        .groupby(date_dimension)
        .select(
            date_dimension.as_(date_dimension_as),
            Property.PropertyType.as_("property_type"),
            fn.Count(Property.ListingId).as_("count_inventory"),
        )
    )

    return q


def sales_price_vs_list_price(options):
    date_dimension, date_dimension_as = get_date_dimension(options["level"])

    q = (
        base_query(options)
        .where(filters.close_date(options))
        .where(filters.mls_status_closed())
        .groupby(date_dimension)
        .select(
            date_dimension.as_(date_dimension_as),
            (fn.Sum(Property.ClosePrice) / fn.Sum(Property.OriginalListPrice)).as_(
                "ratio"
            ),
            metric_median_close_price(date_dimension),
            metric_median_original_list_price(date_dimension),
        )
    )

    return q


def number_of_months_supply_of_homes(options: QueryOptions):
    pass


def major_metrics(options: QueryOptions):
    pass


def inventory_by_number_of_bedrooms(options: QueryOptions):
    q = (
        base_query(options)
        .where(
            filters.on_market_before_end(options)
            & filters.off_market_before_start(options)
        )
        .where(filters.mls_status_active())
        .groupby(Property.BedroomsTotal.as_("bedrooms_total"))
        .select(
            Property.BedroomsTotal.as_("bedrooms_total"),
            fn.Count(Property.ListingId).as_("count"),
        )
    )

    return q


def inventory_by_zipcode(options: QueryOptions):
    q = (
        base_query(options)
        .where(
            filters.on_market_before_end(options)
            & filters.off_market_before_start(options)
        )
        .where(filters.mls_status_active())
        .groupby(Property.PostalCode)
        .select(
            Property.PostalCode.as_("postal_code"),
            fn.Count(Property.ListingId).as_("count"),
        )
    )

    return q


def inventory_by_type_2(options: QueryOptions):
    q = (
        base_query(options)
        .where(
            filters.on_market_before_end(options)
            & filters.off_market_before_start(options)
        )
        .where(filters.mls_status_active())
        .groupby(Property.PropertyType)
        .select(
            Property.PropertyType.as_("property_type"),
            fn.Count(Property.ListingId).as_("count"),
        )
    )

    return q
