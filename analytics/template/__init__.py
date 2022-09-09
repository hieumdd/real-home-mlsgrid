from pathlib import Path

from jinja2 import Environment, FileSystemLoader

template_root_path = Path(__file__).parent
template_env = Environment(
    loader=FileSystemLoader(template_root_path),
    lstrip_blocks=True,
    trim_blocks=True,
)
template_env.filters["quote"] = lambda x: f"'{x}'"


routes = {
    page: {
        path: template_env.get_template(f"{page}/{path}.sql.j2") for path in templates
    }
    for page, templates in [
        (
            "dimension",
            [
                "country",
                "city",
            ],
        ),
        (
            "location",
            [
                "median-average-house-price",
                "sales-price-vs-list-price-ratio",
                "inventory-by-type",
                "major-metrics",
                "inventory",
            ],
        ),
        (
            "supply-demand",
            [
                "absorbtion-rate",
                "closed-sales-vs-under-contract",
                "new-listing-vs-under-contract",
                "days-on-market",
            ],
        ),
        (
            "price-reduction",
            [
                "price-reduction",
            ],
        ),
    ]
}
