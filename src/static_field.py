
from abc import ABC
from typing import Iterable

from .field import Field
from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Parseable,
)


class StaticField(Field):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        StaticField.parse(self, self.line)

    def __str__(self):
        return self.as_class_variable()

    def as_class_variable(self, tabs=1) -> str:
        tabs = '\t' * tabs
        return f'{tabs}{self.name}: {self.return_type}'



