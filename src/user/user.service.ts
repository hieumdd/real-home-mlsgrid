import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@mikro-orm/nestjs';
import { EntityRepository } from '@mikro-orm/core';
import { EntityManager } from '@mikro-orm/postgresql';

import { User, Feature } from './user.entity';
import { CreateUserDto } from './user.dto';

@Injectable()
export class UserService {
    constructor(
        readonly em: EntityManager,

        @InjectRepository(User)
        private userRepository: EntityRepository<User>,
    ) {}

    async findOrCreateUser(email: string) {
        return this.findOneByEmail(email).catch(async () => {
            const user = this.userRepository.create({ email });
            await this.userRepository.persistAndFlush(user);
            return user;
        });
    }

    findOne(id: number) {
        return this.userRepository.findOneOrFail({ id });
    }

    findOneByEmail(email: string) {
        return this.userRepository.findOneOrFail({ email });
    }

    async upsert(createUserDto: CreateUserDto) {
        return this.userRepository
            .findOneOrFail({ id: createUserDto.id })
            .then((user) => {
                this.userRepository.assign(user, createUserDto);
                return user;
            })
            .catch(() => {
                const user = this.userRepository.create(createUserDto);
                this.userRepository.persist(user);
                return user;
            });
    }

    async seed() {
        const dtos = [
            {
                id: 1,
                email: 'hieumdd@gmail.com',
                features: [Feature.DemandPlanning, Feature.DataService],
            },
        ];

        return this.em
            .createQueryBuilder(User)
            .insert(dtos)
            .onConflict(['id'])
            .merge()
            .then(() => this.userRepository.count());
    }
}
