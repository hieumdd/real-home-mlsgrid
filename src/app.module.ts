import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { RouterModule } from '@nestjs/core';
import { ScheduleModule } from '@nestjs/schedule';

import { DatabaseModule } from './database/database.module';
import { AnalyticsModule } from './analytics/analytics.module';

const routes = [
    {
        path: 'analytics',
        module: AnalyticsModule,
    },
];

@Module({
    imports: [
        ConfigModule.forRoot(),
        ScheduleModule.forRoot(),
        DatabaseModule,
        ...routes.map(({ module }) => module),
        RouterModule.register(routes),
    ],
})
export class AppModule {}
