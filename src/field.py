import re
from abc import ABC
from typing import Iterable, AnyStr

from .parameter import Parameter
from .typelike import Typelike
from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Parseable,
)


class Field(Memorable, Parseable):
    name: str
    return_type: Typelike

    re_field = re.compile(r".* : ([_&\w.-]+) \(type: ([^<\[)]+)([^)]+)?\)\n")
    re_field_name = re.compile(r".* : ([_&\w.-]+).*")

    def __init__(self, **kwargs):
        self.name = ''
        super().__init__(**kwargs)
        Field.parse(self, line=self.line)
        self._imports.append(self.return_type)

    def __str__(self):
        return self.as_instance_variable()

    def as_instance_variable(self, tabs=2) -> str:
        return self._as_instance_variable(
            tabs=tabs,
            name=self.name,
            return_type=self.return_type
        )

    @staticmethod
    def _as_instance_variable(name: str,
                              return_type: Typelike | str,
                              tabs: int = 2) -> str:
        tabs_str: str = '\t' * tabs
        return f'{tabs_str}self.{name}: {return_type} = {name}'

    def parse(self, line: str, **kwargs) -> None:
        self.name, self.return_type = self._parse(line=line, **kwargs)

    @staticmethod
    def _parse(line: str, **kwargs) -> [str, Typelike]:
        match = re.match(Field.re_field, line)
        name = match.group(1)
        if match.group(3):
            return_type = Typelike(fragment=(match.group(2) + match.group(3)))
        else:
            return_type = Typelike(fragment=match.group(2))
        return name, return_type

    def as_parameter(self) -> str:
        return self._as_parameter(self.name, self.return_type)

    @staticmethod
    def _as_parameter(name: str, return_type: Typelike) -> str:
        return f'{name}: {return_type}'



