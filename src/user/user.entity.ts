import { Entity, Property, Enum } from '@mikro-orm/core';

import { Record } from '../common/entity';

export enum Feature {
    DemandPlanning = 'demand-planning',
    DataService = 'data-service',
}

@Entity()
export class User extends Record {
    @Property()
    email: string;

    @Enum({ items: () => Feature, array: true, default: [] })
    features: Feature[] = [];
}
