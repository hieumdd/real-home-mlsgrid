import { Controller, Get, Query } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';

import { AnalyticsService } from './analytics.service';
import { QueryLevelByDto } from './analytics.dto';

const route = 'price-reduction';

@ApiTags('Analytics / Price Reduction')
@Controller(`/${route}`)
export class PriceReductionController {
    constructor(private readonly analyticsService: AnalyticsService) {}

    @Get('price-reduction')
    async priceReductionPriceReduction(@Query() options: QueryLevelByDto) {
        return this.analyticsService.query(`${route}/price-reduction`, options);
    }
}
