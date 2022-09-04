from analytics.repo import (
    location_analysis,
    supply_demand_analysis_1,
    supply_demand_analysis_2,
    price_reduction,
)

location_analysis_routes = {
    "median-average-house-price": location_analysis.median_average_house_price,
    "sales-price-vs-original-price-ratio": location_analysis.sales_price_vs_original_price_ratio,
    "inventory-by-type": location_analysis.inventory_by_type,
    "number-of-months-supply-of-homes": location_analysis.number_of_months_supply_of_homes,
    "major-metrics": location_analysis.major_metrics,
    "inventory-by-number-of-bedrooms": location_analysis.inventory_by_number_of_bedrooms,
    "inventory-by-zipcode": location_analysis.inventory_by_zipcode,
    "inventory-by-type-2": location_analysis.inventory_by_type_2,
}

supply_demand_analysis_1_routes = {
    "new-listing-vs-under-contract": supply_demand_analysis_1.new_listing_vs_under_contract,
    "absorption-rate": supply_demand_analysis_1.absorption_rate,
}

supply_demand_analysis_2_routes = {
    "days-on-market": supply_demand_analysis_2.days_on_market,
    "days-on-market-by-number-of-bedrooms": supply_demand_analysis_2.days_on_market_by_number_of_bedrooms,
    "days-on-market-by-type": supply_demand_analysis_2.days_on_market_by_type,
    "under-contract-vs-closed-sales": supply_demand_analysis_2.under_contract_vs_closed_sales,
    "under-contract-vs-closed-sales-by-number-of-bedrooms": supply_demand_analysis_2.under_contract_vs_closed_sales_by_number_of_bedrooms,
    "under-contract-vs-closed-sales-by-type": supply_demand_analysis_2.under_contract_vs_closed_sales_by_type,
}

price_reduction_routes = {
    "avg-time-to-discount": price_reduction.avg_time_to_discount,
    "avg-time-to-discount-by-number-of-bedrooms": price_reduction.avg_time_to_discount_by_number_of_bedrooms,
    "avg-time-to-discount-by-type": price_reduction.avg_time_to_discount_by_type,
    "avg-price-reduction": price_reduction.avg_price_reduction,
    "avg-price-reduction-by-number-of-bedrooms": price_reduction.avg_price_reduction_by_number_of_bedrooms,
    "avg-price-reduction-by-type": price_reduction.avg_price_reduction_by_type,
}

routes = (
    location_analysis_routes
    | supply_demand_analysis_1_routes
    | supply_demand_analysis_2_routes
    | price_reduction_routes
)
