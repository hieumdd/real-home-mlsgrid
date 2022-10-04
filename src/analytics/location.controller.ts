import { Controller, Get, Query } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';

import { AnalyticsService } from './analytics.service';
import { QueryBaseDto, QueryLevelDto, QueryByDto } from './analytics.dto';

const route = 'location';

@ApiTags('Analytics / Location')
@Controller(`/${route}`)
export class LocationController {
    constructor(private readonly analyticsService: AnalyticsService) {}

    @Get(`median-average-house-price`)
    async locationMedianAverageHousePrice(@Query() options: QueryLevelDto) {
        return this.analyticsService.query(
            `${route}/median-average-house-price`,
            options,
        );
    }

    @Get(`sales-price-vs-list-price-ratio`)
    async locationSalesPriceVsListPriceRatio(@Query() options: QueryLevelDto) {
        return this.analyticsService.query(
            `${route}/sales-price-vs-list-price-ratio`,
            options,
        );
    }

    @Get(`inventory-by-type`)
    async locationInventoryByType(@Query() options: QueryLevelDto) {
        return this.analyticsService.query(
            `${route}/inventory-by-type`,
            options,
        );
    }

    @Get(`major-metrics-total-avg-sales-list-days-to-close`)
    async locationMajorMetricsTotalAvgSalesListDaysToClose(
        @Query() options: QueryBaseDto,
    ) {
        return this.analyticsService.query(
            `${route}/major-metrics-total-avg-sales-list-days-to-close`,
            options,
        );
    }

    @Get(`major-metrics-residential-sales-volume`)
    async locationMajorMetricsResidentialSalesVolume(
        @Query() options: QueryBaseDto,
    ) {
        return this.analyticsService.query(
            `${route}/major-metrics-residential-sales-volume`,
            options,
        );
    }

    @Get(`major-metrics-condo-sales-volume`)
    async locationMajorMetricsCondoSalesVolume(@Query() options: QueryBaseDto) {
        return this.analyticsService.query(
            `${route}/major-metrics-condo-sales-volume`,
            options,
        );
    }

    @Get(`major-metrics-days-to-market`)
    async locationMajorMetricsDaysToMarket(@Query() options: QueryBaseDto) {
        return this.analyticsService.query(
            `${route}/major-metrics-days-to-market`,
            options,
        );
    }

    @Get(`major-metrics-current-inventory`)
    async locationMajorMetricsCurrentInventory(
        @Query() options: QueryLevelDto,
    ) {
        return this.analyticsService.query(
            `${route}/major-metrics-current-inventory`,
            options,
        );
    }

    @Get(`inventory`)
    async locationInventory(@Query() options: QueryByDto) {
        return this.analyticsService.query(`${route}/inventory`, options);
    }
}
