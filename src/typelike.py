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
    re_shorthands = re.compile(r"[\w.&_-]+\[\]")

    def __init__(self, **kwargs):
        self.generics = []
        self.location = ''
        self.name = ''
        self.return_type = ''
        super().__init__(**kwargs)
        Typelike.parse(self, fragment=self.fragment)

    def __str__(self):
        if self.generics:
            if len(self.generics) > 1:
                return f'{self.path}[{", ".join(str(gen) for gen in self.generics)}]'
            else:
                return f'{self.path}[{str(self.generics[0])}]'
        else:
            return self.path

    @staticmethod
    def find_generics(fragment: str) -> list[str]:
        return re.findall(Typelike.re_generic_contents, fragment)

    @staticmethod
    def replace_list_shorthands(fragment: str) -> str:
        return re.subn(Typelike.re_shorthands, lambda match: f'list[{match.group(1)}]', fragment)[0]

    def parse(self, fragment: str = None, lines: Iterable[str] = None, line: str = None, **kwargs) -> None:
        stripped = self.stripped(fragment)
        name_match = re.match(self.re_generic_name, stripped)
        contents_match = re.match(self.re_generic_contents, stripped)

        self.name = name_match.group(1)
        if contents_match:
            generics_contents = contents_match.group(1)
            self.generics = [Typelike(fragment=gen) for gen in re.findall(self.re_generic, generics_contents)]
        else:
            self.generics = []

        # generics_list is at most one item long, just keeping it this way so regex isn't being a pain
