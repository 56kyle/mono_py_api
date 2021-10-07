
from typing import Iterable

from field import Field
from static_field import StaticField
from method import Method
from abc import ABC
from mixins import (
    Memorable,
    Importable,
    Kwargable,
    Childlike,
    Parseable,
)


class Klass(ABC, Parseable, Memorable, Importable, Kwargable):
    static_fields: list[StaticField]
    fields: list[Field]
    methods: list[Method]
    base_class: object | None

    def __init__(self, **kwargs):
        self.static_fields: list[StaticField] = []
        self.fields: list[Field] = []
        self.methods: list[Method] = []
        self.base_class: Klass | None = None
        self.parents: list[Klass] = []
        super().__init__(**kwargs)

    def static_field_lines(self, tabs=1, **kwargs) -> Iterable[str]:
        for static_field in self.static_fields:
            yield static_field.as_line(tabs=tabs)

    def field_lines(self, tabs=1, **kwargs) -> Iterable[str]:
        for field in self.fields:
            yield field.as_line(tabs=tabs)

    def method_lines(self, tabs=1, **kwargs) -> Iterable[str]:
        for method in self.methods:
            yield method.as_line(tabs=tabs)

    def parse(self, lines, **kwargs) -> str:
        

class BaseKlass(Klass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.static_fields = []
        self.fields = []
        self.methods = []
        self.base_class = None



