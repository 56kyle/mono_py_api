
from abc import ABC
from typing import Iterable

from .static_field import StaticField
from .field import Field
from .method import Method
from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Childlike,
    Parseable,
)


class Klass(Importable, Kwargable):
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
        self.name: str = ''
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

    def as_line(self, tabs=0):
        tabs = '\t' * tabs
        return f'{tabs}class {self.name}'

    def parse(self, **kwargs) -> None:
        section = ''
        for line in self.lines:
            tabs = line.count('\t')
            match tabs:
                case 2:
                    self.line = line
                case 3:
                    section = line
                case 4:
                    match section:
                        case 'static field':
                            self.static_fields.append(StaticField(line=line))
                        case 'field':
                            self.fields.append(Field(line=line))
                        case 'method':
                            self.methods.append(Method(line=line))
                        case 'base_class':
                            self.base_class = BaseKlass(line=line)

    def _import(self):
        pass


class BaseKlass(Klass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.static_fields = []
        self.fields = []
        self.methods = []
        self.base_class = None



