import os
from abc import ABC
from typing import Iterable

from .static_field import StaticField
from .typelike import Typelike
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
        self.as_type: Typelike | None = None
        self.base_class: Typelike | None = None
        self.parents: list[Typelike] = []
        self.name: str = ''
        super().__init__(**kwargs)
        Klass.parse(self, lines=self.lines)

    def __str__(self) -> str:
        return self.as_whole_class()

    def static_field_lines(self, tabs=1, **kwargs) -> Iterable[str]:
        for static_field in self.static_fields:
            yield static_field.as_class_variable(tabs=tabs)

    def as_whole_class(self, tabs=0) -> str:
        tabs_str: str = tabs * "\t"
        class_lines = [
            f'{tabs_str}class {self.name}{self.get_parents_str()}:',
            *self.static_field_lines(tabs=tabs + 1),
            self.get_init(tabs=tabs + 1),
            *[str(method) for method in self.methods]
        ]
        return '\n\n'.join(class_lines)

    def get_init(self, tabs) -> str:
        tabs_str: str = tabs * "\t"
        if self.get_init_parameters():
            init_lines = [
                f'{tabs_str}def __init__(self, {self.get_init_parameters()}):'
            ]
        else:
            init_lines = [
                f'{tabs_str}def __init__(self):',
                f'{tabs_str}\tpass',
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
                    if not self.name:
                        print(lines)
                        print(line)
                    if '<' in line:
                        self.as_type = Typelike(fragment=self.full_path)
                        self._imports.append(self.as_type)
                case 3:
                    section = self.stripped(line)
                case 4:
                    match section:
                        case 'static fields':
                            new_static = StaticField(line=line)
                            self.static_fields.append(new_static)
                            self._imports.append(new_static)
                        case 'fields':
                            new_field = Field(line=line)
                            self.fields.append(new_field)
                            self._imports.append(new_field)
                        case 'methods':
                            new_method = Method(line=line)
                            self.methods.append(new_method)
                            self._imports.append(new_method)
                        case 'base_class':
                            base_class: Typelike = Typelike(fragment=self.stripped(line).split(' : ')[-1])
                            self.base_class = base_class
                            self._imports.append(base_class)


