
import pytest
from src.dll import Dll


class TestDll:
    dll_lines = [
                '\t24ad6b7e020 : System\n',
                '\t\t24ad6b7e080 : System.ArraySpec\n',
                    '\t\t\tstatic fields\n',
                    '\t\t\tfields\n',
                        '\t\t\t\t10 : dimensions (type: System.Int32)\n',
                        '\t\t\t\t14 : bound (type: System.Boolean)\n',
                    '\t\t\tmethods\n',
                        '\t\t\t\t24b67bb3e70 : .ctor (dimensions: System.Int32, bound: System.Boolean) -> System.Void\n',
                        '\t\t\t\t24b67bb3f10 : Append (sb: System.Text.StringBuilder) -> System.Text.StringBuilder\n',
                        '\t\t\t\t24b67bb3ec0 : Resolve (type: System.Type) -> System.Type\n',
                        '\t\t\t\t24b67bb3f60 : ToString () -> System.String\n',
                    '\t\t\tbase_class\n',
                        '\t\t\t\t249677d4d30 : System.Object\n',
                '\t\t24ad6763130 : System.ArrayTypeMismatchException\n',
                    '\t\t\tstatic fields\n',
                    '\t\t\tfields\n',
                    '\t\t\tmethods\n',
                        '\t\t\t\t24b3cde2820 : .ctor () -> System.Void\n',
                        '\t\t\t\t24b3cde2870 : .ctor (info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> System.Void\n',
                    '\t\t\tbase_class\n',
                        '\t\t\t\t24a8a402d90 : System.SystemException\n'
            ]

    @pytest.fixture(scope='class', autouse=True)
    def dll(self):
        return Dll(
            lines=self.dll_lines
        )

    def test_dll_is_memorable(self, dll):
        assert dll.address == '24ad6b7e020'

    def test_dll_is_parseable(self, dll):
        assert dll.line == self.dll_lines[0]
        assert dll.lines == self.dll_lines

    def test_dll_str(self, dll):
        assert str(dll) == ''






