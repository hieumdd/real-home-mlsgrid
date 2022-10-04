import { ApiProperty, ApiPropertyOptional } from '@nestjs/swagger';

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
    @ApiProperty()
    level: string;
}

export class QueryByDto extends QueryBaseDto {
    @ApiProperty()
    by: string;
}

export class QueryLevelByDto
    extends QueryBaseDto
    implements QueryLevelDto, QueryByDto
{
    @ApiProperty()
    level: string;

    @ApiProperty()
    by: string;
}
