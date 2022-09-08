import os
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from analytics.repo.common import QueryOptions


template_root_path = Path(__file__).parent
template_env = Environment(
    loader=FileSystemLoader(template_root_path),
    lstrip_blocks=True,
    trim_blocks=True,
)
template_env.filters["quote"] = lambda x: f"'{x}'"


def query(template_path: str):
    def _query(options: QueryOptions):
        template = template_env.get_template(template_path)

        return template.render(options)

    return _query


def multi_level_query(page_name: str, chart_name: str):
    def _query(options: QueryOptions):
        level = options["level"]

        template_paths = os.path.join(page_name, chart_name)

        if level == "month":
            template_path = os.path.join(template_paths, "month.sql.j2")
        elif level == "week":
            template_path = os.path.join(template_paths, "week.sql.j2")
        else:
            template_path = os.path.join(template_paths, "day.sql.j2")

        template = template_env.get_template(template_path)

        return template.render(
            start=options["start"],
            end=options["end"],
            country=options.get("country"),
            city=options.get("city"),
        )

    return _query


def single_level_query(page_name: str, chart_name: str):
    def _query(options: QueryOptions):
        template_path = os.path.join(page_name, chart_name, "query.sql.j2")

        template = template_env.get_template(template_path)

        return template.render(
            start=options["start"],
            end=options["end"],
            country=options.get("country"),
            city=options.get("city"),
        )

    return _query
