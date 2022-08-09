from typing import Callable
from dataclasses import dataclass, field

@dataclass
class Pipeline:
    name: str
    resource: str
    transform: Callable[[list[dict]], list[dict]]
    schema: list[dict]
    select: dict = field(default_factory=dict)
