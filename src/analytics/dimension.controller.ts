import { Controller, Get } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';

import { AnalyticsService } from './analytics.service';

const route = 'dimension';

@ApiTags('Analytics / Dimension')
@Controller(`/${route}`)
export class DimensionController {
    constructor(private readonly analyticsService: AnalyticsService) {}

    @Get(`county`)
    async dimensionCounty() {
        return this.analyticsService.query(`${route}/county`);
    }

    @Get(`city`)
    async dimensionCity() {
        return this.analyticsService.query(`${route}/city`);
    }
}
