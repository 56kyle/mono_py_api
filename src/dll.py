from abc import ABC, abstractmethod
from typing import Iterable

from .klass import Klass
from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Childlike,
    Parseable,
)


class Dll(Memorable, Kwargable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.classes: [Klass] = []

    def parse(self, lines: Iterable[str], **kwargs) -> None:
        class_section = []
        for line in lines:
            tabs = line.count('\t')
            if tabs == 1:
                self.line = line
            elif tabs == 2:
                if class_section:
                    self.classes.append(Klass(lines=class_section))
                class_section = [self.line]
            else:
                class_section.append(line)











