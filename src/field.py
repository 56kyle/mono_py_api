
from abc import ABC
from typing import Iterable

from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Childlike,
    Parseable,
)


class Field(Memorable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

