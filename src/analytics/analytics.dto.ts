import { ApiProperty, ApiPropertyOptional } from '@nestjs/swagger';

const LevelEnum = ['day', 'week', 'month'];

const ByEnum = ['bedrooms', 'type', 'zip_code'];

export class QueryBaseDto {
    @ApiProperty()
    start: string;

    @ApiProperty()
    end: string;

    @ApiPropertyOptional()
    county?: string;

    @ApiPropertyOptional()
    city?: string;
}

export class QueryLevelDto extends QueryBaseDto {
    @ApiProperty({ enum: LevelEnum })
    level: string;
}

export class QueryByDto extends QueryBaseDto {
    @ApiProperty({ enum: ByEnum })
    by: string;
}

export class QueryLevelByDto
    extends QueryBaseDto
    implements QueryLevelDto, QueryByDto
{
    @ApiProperty({ enum: LevelEnum })
    level: string;

    @ApiProperty({ enum: ByEnum })
    by: string;
}

export type QueryOptions =
    | QueryBaseDto
    | QueryLevelDto
    | QueryByDto
    | QueryLevelByDto
    | {};
