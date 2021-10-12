from typing import Generic, TypeVar, Iterable
import re

from src.mixins import Importable, Parseable

T = TypeVar('T')
R = TypeVar('R')
U = TypeVar('U')


class Typelike(Generic[T], Importable, Parseable):
    location: str
    return_type: str

    #re_generic_contents = re.compile(r"<([\w.,<>\[\]_&-]+)>.*")
    re_generic_contents = re.compile(r"[\w.&_-]+<(.+)>")
    re_generic_name = re.compile(r"([\w.&_-]+)(?:<.*>)?")
    re_generic = re.compile(r"[\w.&_-]+(?:<.+>)?")
    re_shorthands = re.compile(r"([\w.&_-]+)\[\]")

    def __init__(self, **kwargs):
        self.generics = []
        self.location = ''
        self.name = ''
        self.return_type = ''
        super().__init__(**kwargs)
        self.line = self.replace_list_shorthands(self.line)
        Typelike.parse(self, fragment=self.fragment)

    def __str__(self):
        if self.generics:
            if len(self.generics) > 1:
                return f'{self.name}[{", ".join(str(gen) for gen in self.generics)}]'
            else:
                return f'{self.name}[{str(self.generics[0])}]'
        else:
            return self.name

    @staticmethod
    def find_generics(fragment: str) -> list[str]:
        return re.findall(Typelike.re_generic_contents, fragment)

    @staticmethod
    def replace_list_shorthands(fragment: str) -> str:
        if fragment and '[]' in fragment:
            fin_line = re.subn(Typelike.re_shorthands, lambda match: f'list<{match.group(1)}>', fragment)[0]
            return fin_line
        else:
            return fragment

    @staticmethod
    def _parse(fragment: str = None, lines: Iterable[str] = None, line: str = None, **kwargs) -> (str, list):
        if not fragment:
            fragment = line
        stripped = Typelike.stripped(fragment)
        stripped = Typelike.replace_list_shorthands(stripped)
        name_match = re.match(Typelike.re_generic_name, stripped)
        contents_match = re.match(Typelike.re_generic_contents, stripped)

        name = name_match.group(1)
        if contents_match:
            generics_contents = contents_match.group(1)
            generics = [Typelike(fragment=gen) for gen in re.findall(Typelike.re_generic, generics_contents)]
        else:
            generics = []

        return name, generics

    def parse(self, fragment: str = None, lines: Iterable[str] = None, line: str = None, **kwargs) -> None:
        self.name, self.generics = self._parse(
            fragment=fragment,
            lines=lines,
            line=line,
            **kwargs
        )
        for gen in self.generics:
            self._imports.append(gen)




