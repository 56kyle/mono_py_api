
from abc import ABC
from typing import Iterable

from .field import Field
from .method import Method
from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Parseable,
)


class StaticField(Field):
    def __init__(self, **kwargs):
        self.parameters = []
        super().__init__(**kwargs)
        StaticField.parse(self, self.line)
        for param in self.parameters:
            self._imports.append(param)

    def __str__(self):
        if self.parameters:
            return self.as_class_method()
        else:
            return self.as_class_variable()

    @staticmethod
    def _parameters_as_str(parameters) -> str:
        if parameters:
            if len(parameters) > 1:
                return 'cls, ' + ', '.join(str(param) for param in parameters)
            else:
                return 'cls, ' + str(parameters[0])
        else:
            return 'cls'

    def parse(self, line: str, **kwargs) -> None:
        if '->' in line:
            self.name, self.return_type, self.parameters = Method._parse(line=line, **kwargs)
        else:
            self.name, self.return_type = Field._parse(line=line, **kwargs)

    def as_class_variable(self, tabs=1) -> str:
        tabs = '\t' * tabs
        return f'{tabs}{self.name}: {self.return_type}'

    def as_class_method(self, tabs=1) -> str:
        tabs = '\t' * tabs
        method_lines = [
            f'{tabs}@classmethod',
            f'{tabs}def {self.name}({self._parameters_as_str(self.parameters)}) -> {self.return_type}:',
            f'{tabs}\tpass'
        ]
        return '\n'.join(method_lines)



