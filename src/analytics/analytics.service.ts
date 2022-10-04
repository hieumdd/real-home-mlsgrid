import { Injectable } from '@nestjs/common';
import * as nunjucks from 'nunjucks';
import { BigQueryDate } from '@google-cloud/bigquery';
import { chain } from 'lodash';

import { BigQueryProvider } from '../google-cloud/bigquery.service';

@Injectable()
export class AnalyticsService {
    private env: nunjucks.Environment;

    constructor(private bigqueryProvider: BigQueryProvider) {
        const loader = new nunjucks.FileSystemLoader(`${__dirname}/template`);
        this.env = new nunjucks.Environment(loader, { autoescape: false });
        this.env.addFilter('quote', (value) => `'${value}'`);
    }

    render(path: string, options: any) {
        return this.env.render(path, options);
    }

    async query(path: string, options: any) {
        const sql = this.render(path, options);
        return this.bigqueryProvider
            .query<any>(sql)
            .then((rows) => {
                const parse = (value: any) =>
                    value instanceof BigQueryDate ? value.value : value;

                return rows.map((row) => chain(row).mapValues(parse).value());
            })
            .then((data) => ({ data }));
    }
}
