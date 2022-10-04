import { Feature } from './user.entity';

export class CreateUserDto {
    id?: number;

    email: string;

    features: Feature[];
}
