import { Injectable } from '@nestjs/common';
import { EntityManager } from '@mikro-orm/postgresql';
import { Seeder } from '@mikro-orm/seeder';

import { User } from './user.entity';
import { UserService } from './user.service';

@Injectable()
export class UserSeeder extends Seeder {
    async run(em: EntityManager) {
        const userService = new UserService(em, em.getRepository(User));

        await userService.seed();
    }
}
