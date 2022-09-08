from pathlib import Path

from jinja2 import Environment, FileSystemLoader


template_root_path = Path(__file__).parent
template_env = Environment(
    loader=FileSystemLoader(template_root_path),
    lstrip_blocks=True,
    trim_blocks=True,
)
template_env.filters["quote"] = lambda x: f"'{x}'"
