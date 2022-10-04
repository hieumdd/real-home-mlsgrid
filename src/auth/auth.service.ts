import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { JwtService } from '@nestjs/jwt';

import { UserService } from '../user/user.service';
import { Token } from './token.interface';
import { TokenDto } from './token.dto';

@Injectable()
export class AuthService {
    constructor(
        private readonly configService: ConfigService,
        private readonly jwtService: JwtService,
        private readonly userService: UserService,
    ) {}

    getJwt(id: number): string {
        return this.jwtService.sign(<Token>{ id });
    }

    getUserFromJwt(token: string, ignoreExpiration = false) {
        const payload = this.jwtService.verify<Token>(token, {
            ignoreExpiration,
        });
        return this.userService.findOne(payload.id);
    }

    async refreshJwt({ token }: TokenDto) {
        return this.getUserFromJwt(token, true).then((user) => ({
            user,
            token: this.getJwt(user.id),
        }));
    }
}
