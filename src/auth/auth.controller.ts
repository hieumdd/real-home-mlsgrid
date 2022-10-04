import { Controller, Post, Body } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';

import { AuthService } from './auth.service';
import { GoogleAuthService } from './google-auth.service';
import { TokenDto } from './token.dto';

@ApiTags('Auth')
@Controller()
export class AuthController {
    constructor(
        private readonly authService: AuthService,
        private readonly googleAuthService: GoogleAuthService,
    ) {}

    @Post('google')
    async authenticate(@Body() tokenData: TokenDto) {
        return this.googleAuthService
            .authenticate(tokenData.token)
            .then((user) => ({
                user,
                token: this.authService.getJwt(user.id),
            }));
    }

    @Post('refresh')
    refresh(@Body() tokenData: TokenDto) {
        return this.authService.refreshJwt(tokenData);
    }
}