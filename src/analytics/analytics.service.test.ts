import { Test, TestingModule } from '@nestjs/testing';
import { BigQueryDate } from '@google-cloud/bigquery'
import { AnalyticsModule } from './analytics.module';
import { AnalyticsService } from './analytics.service';

jest.setTimeout(60_000);

describe('Analytics', () => {
    let moduleRef: TestingModule;
    let analyticsService: AnalyticsService;

    beforeAll(async () => {
        moduleRef = await Test.createTestingModule({
            imports: [AnalyticsModule],
        }).compile();

        analyticsService = moduleRef.get(AnalyticsService);
    });

    afterAll(async () => {
        await moduleRef.close();
    });

    describe('Query', () => {
        it('Query', async () => {
            const options = {
                level: 'day',
                by: 'type',
                start: '2022-01-01',
                end: '2022-02-01',
            };
            const res = await analyticsService.query('supply-demand/days-on-market.sql.j2', options);
            expect(res).toBeTruthy();
        });
    });
});
