import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { RouterModule } from '@nestjs/core';
import { ScheduleModule } from '@nestjs/schedule';

import { DatabaseModule } from './database/database.module';
import { NetSuiteModule } from './netsuite/netsuite.module';
import { AuthModule } from './auth/auth.module';
import { UserModule } from './user/user.module';
import { DemandPlanningModule } from './demand-planning/demand-planning.module';
import { DataLookupModule } from './data-lookup/data-lookup.module';
import { DataServiceModule } from './data-service/data-service.module';
import { StoreTrafficModule } from './store-traffic/store-traffic.module';

const routes = [
    {
        path: 'auth',
        module: AuthModule,
    },
    {
        path: 'user',
        module: UserModule,
    },
    {
        path: 'netsuite',
        module: NetSuiteModule,
    },
    {
        path: 'demand-planning',
        module: DemandPlanningModule,
    },
    {
        path: 'data-lookup',
        module: DataLookupModule,
    },
    {
        path: 'store-traffic',
        module: StoreTrafficModule,
    },
    {
        path: 'data-service',
        module: DataServiceModule,
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
