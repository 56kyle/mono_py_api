
from typing import Iterable

from abc import ABC
from mixins import (
    Memorable,
    Importable,
    Kwargable,
    Childlike,
    Parseable,
)


class Method(ABC, Memorable, Kwargable, Parseable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

