import re

from .mixins import Parseable
from .typelike import Typelike


class Parameter(Parseable):
    name: str
    return_type: Typelike

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Parameter.parse(self, fragment=self.fragment)
        self._imports.append(self.return_type)

    def __str__(self):
        return f'{self.name}: {self.return_type}'

    def parse(self, fragment: str, **kwargs) -> None:
        # line - 'foo: bar.baz.boo<bad.thing.sue<System.Int32>>'
        self.name, return_type = fragment.split(': ')
        self.return_type = Typelike(fragment=return_type)

    def as_parameter(self) -> str:
        return f'{self.name}: {self.return_type}'

