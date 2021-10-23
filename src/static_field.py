
import re

from abc import ABC
from typing import Iterable

from .field import Field
from .method import Method
from .parameter import Parameter
from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Parseable,
)
from .typelike import Typelike


class StaticField(Memorable):
    name: str
    return_type: Typelike
    re_field = re.compile(r".* : ([_&\w.-]+) \(type: ([^<\[)]+)([^)]+)?\)\n")
    re_field_name = re.compile(r".* : ([_&\w.-]+).*")

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

    @staticmethod
    def _as_parameter(name: str, return_type: Typelike) -> str:
        return f'{name}: {return_type}'

    def as_parameter(self) -> str:
        return self._as_parameter(self.name, self.return_type)

    def parse(self, line: str, **kwargs) -> None:
        if '->' in line:
            self.name, self.return_type, self.parameters = Method._parse(line=line, **kwargs)
        else:
            self.name, self.return_type = Field._parse(line=line, **kwargs)

    @staticmethod
    def _as_class_variable(name: str, return_type: Typelike, tabs=1) -> str:
        tabs = '\t' * tabs
        return f'{tabs}{name}: {return_type}'

    def as_class_variable(self, tabs=1) -> str:
        return self._as_class_variable(
            name=self.name,
            return_type=self.return_type,
            tabs=tabs
        )

    @staticmethod
    def _as_class_method(name: str, return_type: Typelike, parameters: list[Parameter], tabs=1) -> str:
        tabs = '\t' * tabs
        method_lines = [
            f'{tabs}@classmethod',
            f'{tabs}def {name}({StaticField._parameters_as_str(parameters)}) -> {return_type}:',
            f'{tabs}\tpass'
        ]
        return '\n'.join(method_lines)

    def as_class_method(self, tabs=1) -> str:
        return self._as_class_method(
            name=self.name,
            return_type=self.return_type,
            parameters=self.parameters,
            tabs=tabs
        )
