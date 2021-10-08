
from abc import ABC
from typing import Iterable

from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Parseable,
)


class Method(Memorable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Method.parse(self, line=self.line)

    def parse(self, line: str, **kwargs):
        pass

