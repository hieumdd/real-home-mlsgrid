import { Module } from '@nestjs/common';

import { GoogleCloudModule } from '../google-cloud/google-cloud.module';
import { AnalyticsService } from './analytics.service';

@Module({
    imports: [GoogleCloudModule],
    providers: [AnalyticsService],
})
export class AnalyticsModule {}
