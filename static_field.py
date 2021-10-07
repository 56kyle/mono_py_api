
from typing import Iterable

from abc import ABC
from mixins import (
    Memorable,
    Importable,
    Kwargable,
    Childlike,
    Parseable,
)


class StaticField(ABC, Memorable, Kwargable, Parseable):
    def __init__(self):
        pass

