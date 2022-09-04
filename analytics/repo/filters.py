from analytics.repo.common import QueryOptions, Property


def close_date(options: QueryOptions):
    return Property.CloseDate[options["start"] : options["end"]]  # type: ignore


def on_market_before_end(options: QueryOptions):
    return Property.OnMarketDate <= options["end"]


def off_market_before_start(options: QueryOptions):
    start = options["start"]
    return (Property.OffMarketDate >= start) | (Property.ContingentDate >= start)

def mls_status_closed():
    return Property.MlsStatus == "Closed"


def mls_status_active():
    return Property.MlsStatus.isin(
        [
            "Active",
            "Coming Soon / Hold",
            "Under Contract - Showing",
            "Under Contract - Not Showing",
            "Closed",
        ]
    )
