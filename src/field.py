import re
from abc import ABC
from typing import Iterable

from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Parseable,
    Typelike,
)


class Field(Memorable):
    name: str
    return_type: Typelike
    re_field = re.compile(r".* : ([_&\w.-]+) \(type: ([^<\[)]+)([^)]+)?\)\n")

    def __init__(self, **kwargs):
        self.name = ''
        super().__init__(**kwargs)
        Field.parse(self, line=self.line)

    def __str__(self):
        return f'\t\tself.{self.name}: {self.return_type} = {self.name}'

    def as_line(self, tabs=0) -> str:
        return str(self)

    def parse(self, line: str, **kwargs) -> None:
        match = re.match(self.re_field, line)
        self.name = match.group(1)
        if match.group(3):
            self.return_type = Typelike(line=(match.group(2) + match.group(3)))
        else:
            self.return_type = Typelike(line=match.group(2))


