import { ExecutionContext, UseGuards, mixin } from '@nestjs/common';

import { Feature } from '../user/user.entity';
import { RequestWithUser } from './request-with-user.interface';
import { JwtGuard } from './jwt.guard';

export const FeatureGuard = (feature: Feature) => () => {
    class FeatureGuardMixin extends JwtGuard {
        async canActivate(context: ExecutionContext) {
            await super.canActivate(context);

            const request = context
                .switchToHttp()
                .getRequest<RequestWithUser>();
            const user = request.user;

            return user?.features.includes(feature);
        }
    }

    return UseGuards(mixin(FeatureGuardMixin));
};
