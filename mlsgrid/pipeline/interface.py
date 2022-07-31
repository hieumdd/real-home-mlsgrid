from typing import Callable
from dataclasses import dataclass

@dataclass
class Pipeline:
    name: str
    resource: str
    transform: Callable[[list[dict]], list[dict]]
    schema: list[dict]
