
from abc import ABC
from typing import Iterable

from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Parseable,
)


class StaticField(Memorable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        StaticField.parse(self, self.line)

    def parse(self, line: str, **kwargs) -> None:
        pass


