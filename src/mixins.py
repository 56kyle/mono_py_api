from abc import ABC, abstractmethod
from keyword import kwlist
from typing import Generic, TypeAlias, NewType, Any, TypeVar, Iterable, AnyStr

import re


class Kwargable:
    """Makes the class accept any key, value pair as an instance variable"""
    kwargs: dict

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kwargs = kwargs
        for k, v in self.kwargs.items():
            setattr(self, k, v)


class Parseable(ABC, Kwargable):
    def __init__(self, lines: Iterable[str] = None, line: str = None, fragment: str = None, **kwargs):
        self.lines = lines
        self.line = line
        self.fragment = fragment
        self._imports: list[Parseable] = []
        if self.lines is None and self.line is None and self.fragment is None:
            raise Exception('Either line or lines or fragment must be passed on init')
        if self.line is None and self.lines:
            self.line = [*self.lines][0]
        super().__init__(**kwargs)
        try:
            for keyword in kwlist:
                if self.name == keyword:
                    print(self.name)
                    self.name = '_' + keyword
        except AttributeError as e:
            pass

    @abstractmethod
    def parse(self, **kwargs) -> None:
        pass

    @staticmethod
    def stripped(line: str) -> str:
        return line.replace('\t', '').replace('\n', '')

    @property
    def imports(self) -> set:
        import_strings = []
        all_imports = []
        for _import in self._imports:
            if isinstance(_import, Importable):
                _import_str = _import.as_import()
            else:
                _import_str = str(_import)

            if _import_str not in import_strings and not _import_str.endswith('.dll'):
                import_strings.append(_import_str)
                for imp in _import.imports:
                    all_imports.append(imp)

        if isinstance(self, Importable):
            return {*[*all_imports, self]}

        return {*all_imports}


class Memorable(Parseable):
    """Mixes in address handling methods and logic"""
    address: str

    def __init__(self, **kwargs):
        self.address = ''
        super().__init__(**kwargs)
        Memorable.parse(self, line=self.line)

    def parse(self, line: str, **kwargs):
        if ' : ' in line:
            self.address = self.stripped(line).split(' : ')[0]
        else:
            self.address = self.stripped(line)


class Importable(Parseable):
    """Mixes in methods for generating import statements"""
    import_path: str
    import_name: str
    path_to_import: str
    path: str = ''
    segments: list[str]
    importables: list

    re_import_name = re.compile(r"([\w._-]+).*")
    re_delegate = re.compile(r"<(.+)>([\w.&_-]+)")

    def __init__(self, **kwargs):
        self.importables = [self]
        super().__init__(**kwargs)
        Importable.parse(self, line=self.line, fragment=self.fragment)

    @staticmethod
    def _parse_imports(
            lines: Iterable[str] = None,
            line: str = None,
            fragment: str = None,
            re_import_name: re.Pattern[str] = None,
            **kwargs
    ):
        line = fragment if not line else fragment
        line = line.replace('[]', '')

        if ' : ' in line:
            line = line.split(' : ')[1]

        line = Importable.stripped(line)
        if line.split('.')[-1].startswith('<'):
            line_segments = line.split('.')
            del line_segments[-1]
            match = re.match(Importable.re_delegate, line.split('.')[-1])
            line = '.'.join([*line_segments, f'{match.group(2)}<{match.group(1)}>'])
        elif '<' in line:
            line = line.split('<')[0]

        if '.' in line:
            segments = line.split('.')
        else:
            segments = [line]

        segments_length = len(segments)
        match segments_length:
            case 0:
                raise Exception('Not enough segments to be importable')
            case 1:
                import_path = segments[0]
                import_name = segments[0]
                ref_name = segments[0]
            case 2:
                import_path = segments[0]
                import_name = segments[-1]
                ref_name = '.'.join(segments)
            case _:
                import_path = '.'.join(segments[:-1])
                import_name = segments[-1]
                ref_name = '.'.join(segments[-2:])

        match = re.match(re_import_name, import_name)
        if match:
            import_name = match.group(1)

        ref_match = re.match(re_import_name, ref_name)
        if ref_match:
            ref_name = match.group(1)
        path = '.'.join(segments)
        return import_path, import_name, ref_name, segments, path

    def parse(self, lines: Iterable[str] = None, line: str = None, fragment: str = None, **kwargs) -> None:
        self.import_path, self.import_name, self.ref_name, self.segments, self.path = self._parse_imports(
            lines=lines,
            line=line,
            fragment=fragment,
            re_import_name=self.re_import_name,
            **kwargs
        )

    @staticmethod
    def _as_import(segments: list[str]) -> str:
        return f'import {segments[0]}'

    def as_import(self) -> str:
        return self._as_import(self.segments)


Mixins = [
    Parseable,
    Memorable,
    Importable,
    Kwargable,
]
