from abc import ABC, abstractmethod
from typing import Iterable

from .klass import Klass
from .mixins import (
    Memorable,
    Importable,
    Kwargable,
    Parseable,
)

import os


class Dll(Memorable):
    def __init__(self, **kwargs):
        self.name: str = ''
        self.classes: [Klass] = []
        super().__init__(**kwargs)
        Dll.parse(self, lines=self.lines)

    def __str__(self):
        class_lines = [str(klass) for klass in self.classes]
        all_imports = [_import for _import in self.imports]
        import_lines = set()
        for imp in all_imports:
            if isinstance(imp, Importable):
                if self.name not in imp.name:
                    import_lines.add(imp.as_import())

        dll_lines = [
            *import_lines,
            '\n\n'.join(class_lines),
        ]

        return '\n'.join(dll_lines)

    def parse(self, lines: Iterable[str], **kwargs) -> None:
        class_section = []
        for line in lines:
            tabs = line.count('\t')
            if tabs == 1:
                self.line = line
            elif tabs == 2:
                if class_section:
                    new_klass = Klass(lines=class_section)
                    self.classes.append(new_klass)
                    self._imports.append(new_klass)
                class_section = [line]
            else:
                class_section.append(line)
        self.name = self.stripped(self.line).split(' : ')[-1].replace('.dll', '')


