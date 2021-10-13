import pytest
from src.dll import Dll
from .dll_data import dll_str


class TestDll:
    dll_lines = [dll_string + '\n' for dll_string in dll_str.split('\n')]

    @pytest.fixture(scope='class', autouse=True)
    def dll(self):
        return Dll(
            lines=self.dll_lines
        )

    def test_dll_is_memorable(self, dll):
        assert dll.address == '24a8a6a8f40'

    def test_dll_is_parseable(self, dll):
        assert dll.line == self.dll_lines[0]
        assert dll.lines == self.dll_lines

    def test_dll_str(self, dll):
        print(dll.imports)
        print(str(dll))
        with open('./test.py', 'w') as file:
            file.write(str(dll))






