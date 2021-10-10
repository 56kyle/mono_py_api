
from abc import ABC
from typing import Iterable

from .static_field import StaticField
from .field import Field
from .method import Method
from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Parseable,
)


class Klass(Memorable, Importable):
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
        Klass.parse(self, lines=self.lines)

    def __str__(self) -> str:
        return self.as_whole_class()

    def static_field_lines(self, tabs=1, **kwargs) -> Iterable[str]:
        for static_field in self.static_fields:
            yield static_field.as_class_variable(tabs=tabs)

    def field_lines(self, tabs=1, **kwargs) -> Iterable[str]:
        for field in self.fields:
            yield field.as_instance_variable(tabs=tabs)

    def method_lines(self, tabs=1, **kwargs) -> Iterable[str]:
        for method in self.methods:
            yield method.as_method(tabs=tabs)

    def as_whole_class(self, tabs=0) -> str:
        tabs_str: str = tabs * "\t"
        class_lines = [
            f'{tabs_str}class {self.name}{self.get_parents_str()}:',
            *self.static_field_lines(tabs=tabs + 1),
            self.get_init(tabs=tabs + 1),
        ]
        return '\n'.join(class_lines)

    def get_init(self, tabs) -> str:
        tabs_str: str = tabs * "\t"
        init_lines = [
            f'{tabs_str}def __init__(self, {self.get_init_parameters()}):'
        ]
        for field in self.fields:
            init_lines.append(field.as_instance_variable(tabs=tabs+1))
        return '\n'.join(init_lines)

    def get_init_parameters(self) -> str:
        if self.fields:
            if len(self.fields) > 1:
                return ', '.join(field.as_parameter() for field in self.fields)
            else:
                return self.fields[0].as_parameter()
        return ''

    def get_parents_str(self) -> str:
        if not self.parents:
            return ''
        elif len(self.parents) == 1:
            parents_contents = self.parents[0].import_name
        else:
            parents_contents = ", ".join(parent.name for parent in self.parents)
        return f'({parents_contents})'

    def parse(self, lines: Iterable[str], **kwargs) -> None:
        section = ''
        for line in lines:
            tabs = line.count('\t')
            match tabs:
                case 2:
                    self.line = line
                    self.full_path = self.stripped(line).split(' : ')[1]
                    self.name = self.import_name
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



