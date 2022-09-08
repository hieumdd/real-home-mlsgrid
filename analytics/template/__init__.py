from analytics.template.template_service import template_env

location_routes, supply_demand_routes, price_reduction_routes = [
    {path: template_env.get_template(f"{page}/{path}.sql.j2") for path in templates}
    for page, templates in [
        (
            "location",
            [
                "median-average-house-price",
                "sales-price-vs-list-price-ratio",
                "inventory-by-type",
                "major-metrics",
                "inventory",
            ],
        ),
        (
            "supply-demand",
            [
                "days-on-market",
            ],
        ),
        (
            "price-reduction",
            [
                "price-reduction",
            ],
        ),
    ]
]

routes = location_routes | supply_demand_routes | price_reduction_routes
