import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { RouterModule } from '@nestjs/core';
import { ScheduleModule } from '@nestjs/schedule';

import { DatabaseModule } from './database/database.module';
import { AuthModule } from './auth/auth.module';
import { UserModule } from './user/user.module';

const routes = [
    {
        path: 'auth',
        module: AuthModule,
    },
    {
        path: 'user',
        module: UserModule,
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
