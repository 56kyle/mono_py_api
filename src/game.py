
from abc import ABC, abstractmethod
from typing import Iterable

from .dll import Dll
from .klass import Klass
from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Parseable,
)


class Game(Memorable, Parseable):
    dlls: list[Dll]

    def __init__(self, **kwargs):
        self.dlls = []
        super().__init__(**kwargs)
        Game.parse(self, lines=self.lines)

    def __str__(self):
        return '\n\n'.join(str(dll) for dll in self.dlls)

    def parse(self, lines: Iterable[str] = None, **kwargs) -> None:
        dll_section = None
        for line in lines:
            tabs = line.count('\t')
            match tabs:
                case 0:
                    self.line = line
                case 1:
                    if dll_section:
                        self.dlls.append(Dll(lines=dll_section))
                    dll_section = [line]
                case _:
                    dll_section.append(line)





