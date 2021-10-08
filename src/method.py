
from abc import ABC
from typing import Iterable

from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Parseable,
    Typelike,
)
import re


class Method(Memorable):
    name: str
    return_type: Typelike
    re_method = re.compile(r"")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Method.parse(self, line=self.line)

    def parse(self, line: str, **kwargs):
        pass

