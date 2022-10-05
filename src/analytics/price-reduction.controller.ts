import { Controller, Get, Query } from '@nestjs/common';
import { ApiTags, ApiExtraModels } from '@nestjs/swagger';

import { AnalyticsService } from './analytics.service';
import { QueryLevelBy } from './analytics.dto';

const route = 'price-reduction';

@ApiTags('Analytics / Price Reduction')
@ApiExtraModels(QueryLevelBy)
@Controller(route)
export class PriceReductionController {
    constructor(private readonly analyticsService: AnalyticsService) {}

    @Get('price-reduction')
    async priceReductionPriceReduction(@Query() options: QueryLevelBy) {
        return this.analyticsService.query(`${route}/price-reduction`, options);
    }
}
