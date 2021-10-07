
from abc import ABC
from typing import Iterable

from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Childlike,
    Parseable,
)


class StaticField(Memorable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse(self, line: str, **kwargs) -> None:
        pass


