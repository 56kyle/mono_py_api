from abc import ABC, abstractmethod
from typing import Generic, TypeAlias, NewType, Any, TypeVar, Iterable, List, AnyStr

import re

T = TypeVar('T')
R = TypeVar('R')
U = TypeVar('U')


class Kwargable:
    """Makes the class accept any key, value pair as an instance variable"""
    kwargs: dict

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kwargs = kwargs
        for k, v in self.kwargs.items():
            setattr(self, k, v)


class Parseable(ABC, Kwargable):
    def __init__(self, lines: Iterable[str] = None, line: str = None, **kwargs):
        self.lines = lines
        self.line = line
        if self.lines is None and self.line is None:
            raise Exception('Either line or lines must be passed on init')
        if self.line is None:
            self.line = [*self.lines][0]

        super().__init__(**kwargs)

    @abstractmethod
    def parse(self, **kwargs) -> None:
        pass

    @abstractmethod
    def as_line(self, tabs=0) -> str:
        pass

    @staticmethod
    def stripped(line: str) -> str:
        return line.replace('\t', '').replace('\n', '')


class Memorable(Parseable):
    """Mixes in address handling methods and logic"""
    address: str

    def __init__(self, **kwargs):
        self.address = ''
        super().__init__(**kwargs)
        Memorable.parse(self, line=self.line)

    def as_line(self, tabs=0) -> str:
        return str(self)

    def parse(self, line: str, **kwargs):
        if ' : ' in line:
            self.address = self.stripped(line).split(' : ')[0]
        else:
            self.address = self.stripped(line)


class Importable(Memorable):
    """Mixes in methods for generating import statements"""
    import_path: str
    import_name: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Importable.parse(self, line=self.line)

    def parse(self, line: str, **kwargs):
        if '.' in line:
            segments = line.split('.')
        else:
            segments = [line]

        self.import_path = '.'.join(segments[:-1])
        self.import_name = segments[-1]

    @abstractmethod
    def _import(self):
        pass

    def from_location(self, location: str, **kwargs) -> str:
        _from = []
        if '.' in location:
            location_list: list = location.split('.')
        elif location == self.import_path:
            return '.'
        else:
            location_list: list = [location]

        if '.' in self.import_path:
            import_path_list: list = self.import_path.split('.')
        else:
            import_path_list: list = [self.import_path]

        while import_path_list[0] == location_list[0]:
            _from.append(import_path_list[0])
            del import_path_list[0]
            del location_list[0]
            if not import_path_list or not location_list:
                break
        if not import_path_list:
            return ''
        return '.'.join(import_path_list)

    def import_from(self, location: str, tabs=0, new_lines=1, **kwargs) -> str:
        tabs = "\t" * tabs
        new_lines = "\n" * new_lines
        return f'{tabs}from {self.from_location(location)} import {self.import_path}{new_lines}'

    def normal_import(self, location: str, tabs=0,
                      new_lines=1, **kwargs) -> str:
        tabs = "\t" * tabs
        new_lines = "\n" * new_lines
        from_location = self.from_location(location)
        if from_location == '.':
            pass

        return f'{tabs}import {self.import_path}{new_lines}'


class Typelike(Generic[T], Importable, Parseable):
    location: str
    return_type: str

    re_generic_contents = re.compile(r"[<\[](.+)[>\]]")
    re_shorthands = re.compile(r"([\w.&_-]+)\[\]")

    def __init__(self, **kwargs):
        self.location = ''
        self.name = ''
        self.return_type = ''
        super().__init__(**kwargs)
        Typelike.parse(self, line=self.line)

    def __str__(self):
        return f'{self.import_name}[{", ".join(str(gen) for gen in self.generics)}]'

    @staticmethod
    def find_generics(line: str) -> list[str]:
        return re.findall(Typelike.re_generic_contents, line)

    @staticmethod
    def replace_list_shorthands(line: str) -> str:
        return re.subn(Typelike.re_shorthands, lambda match: f'list[{match.group(1)}]', line)[0]

    def _import(self):
        return self.normal_import(self.location)

    def parse(self, line: str, **kwargs) -> None:
        if '<' in line:
            self.name = self.stripped(line).split('<')[0]
        else:
            self.name = self.stripped(line)
        line = self.replace_list_shorthands(line)
        generics = self.find_generics(line)
        if isinstance(generics, list):
            self.generics = [Typelike(line=gen) for gen in generics]
        elif isinstance(generics, str):
            self.generics = [Typelike(line=generics)]
        else:
            self.generics = []
        print(self.generics)
        super().parse(line=line, **kwargs)

Mixins = [
    Parseable,
    Memorable,
    Importable,
    Kwargable,
    Typelike,
]
