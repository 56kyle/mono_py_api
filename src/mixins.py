from abc import ABC, abstractmethod
from typing import Generic, TypeAlias, NewType, Any, TypeVar, Iterable

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


class Parseable(Kwargable):
    def __init__(self, lines: Iterable[str] = None, line: str = None, **kwargs):
        super().__init__(**kwargs)
        self.lines = lines
        self.line = line
        self.parse()

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
        super().__init__(**kwargs)

    def as_line(self, tabs=0) -> str:
        pass

    def parse(self, **kwargs):
        if ' : ' in self.line:
            self.address = self.line.split(' : ')[0]
        else:
            self.address = self.line


class Importable(Memorable):
    """Mixes in methods for generating import statements"""
    import_path: str
    import_name: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse(self, line: str, **kwargs):
        if '.' in line:
            segments = line.split('.')
        else:
            segments = [line]

        self.import_path = '.'.join(segments[:-1])
        self.import_name = segments[-1]

    @abstractmethod
    def _import(self):
        raise NotImplementedError

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


class Childlike(ABC):
    parent: object

    def __init__(self, parent: object, **kwargs):
        super().__init__(**kwargs)
        self.parent = parent


class Genericlike(ABC, Generic[T]):
    def __init__(self, generics: TypeVar | list[TypeVar], **kwargs):
        super().__init__(**kwargs)
        if isinstance(generics, Iterable):
            self.generics = [*generics]
        else:
            self.generics = [generics]


class Typelike(ABC, Importable):
    def __init__(self, type_name: str, **kwargs):
        super().__init__(**kwargs)
        self.type_name = type_name

    def __str__(self):
        return self.type_name

    def _import(self):
        return self.normal_import(self.location)


Mixins = [
    Parseable,
    Memorable,
    Importable,
    Kwargable,
    Childlike,
    Genericlike,
    Typelike,
]
