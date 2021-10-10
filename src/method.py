
from abc import ABC
from typing import Iterable

from .parameter import Parameter
from .typelike import Typelike
from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Parseable,
)
import re


class Method(Memorable, Parseable):
    name: str
    parameters: list[Parameter]
    return_type: Typelike
    re_method_name = re.compile(r".* : ([\w_.-]+)")
    re_method_param_contents = re.compile(r".* : [\w_.-]+ \(([^()]*)\) -> .*")

    def __init__(self, **kwargs):
        self.parameters: list[Typelike] = []
        super().__init__(**kwargs)
        Method.parse(self, line=self.line)

    def parse(self, line: str, **kwargs) -> None:
        self.name = re.match(self.re_method_name, line).group(1)
        match = re.match(self.re_method_param_contents, line)
        if match:
            param_contents = match.group(1)
            if ', ' in param_contents:
                self.parameters = [Parameter(fragment=param) for param in param_contents.split(', ')]
            else:
                self.parameters = [Parameter(fragment=param_contents)]
        else:
            self.parameters = []

    def as_method(self, tabs=1) -> str:
        tabs_str = '\t' * tabs
        method_lines = [
            f'{tabs_str}def {self.name}({self.parameters_as_str()}) -> {self.return_type}:',
            f'{tabs_str}\tpass'
        ]
        return '\n'.join(method_lines)

    @staticmethod
    def _parameters_as_str(parameters) -> str:
        if parameters:
            if len(parameters) > 1:
                return ', '.join(str(param) for param in parameters)
            else:
                return str(parameters[0])
        else:
            return ''

    def parameters_as_str(self) -> str:
        return self._parameters_as_str(self.parameters)

