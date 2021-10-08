
import pytest
from src.method import Method


class TestMethod:
    def test_simple_method(self):
        Method(line='\t\t\t\t10 : dimensions (type: System.Int32)\n')

    def test_method_with_generic_type(self):
        Method(line='\t\t\t\t0 : Item1 (type: T1)\n')

    def test_method_with_type_containing_generic(self):
        Method(line='\t\t\t\t18 : values (type: System.Object[])\n')


class TestMethodMixins:
    @pytest.fixture(scope='class')
    def method(self):
        return Method(line='\t\t\t\t24b67a72990 : remove_ReconnectingEvent (value: System.Action<System.Collections.Generic.IEnumerable<System.Threading.Tasks.Task<System.Int32>>>) -> System.Void')

    def test_method_is_memorable(self, method: Method):
        assert method.address == '24b67a72990'

    def test_method_is_parseable(self, method: Method):
        assert method.line == '\t\t\t\t24b67a72990 : remove_ReconnectingEvent (value: System.Action<System.Collections.Generic.IEnumerable<System.Threading.Tasks.Task<System.Int32>>>) -> System.Void'
        assert method.lines is None
        assert method.as_line() == f'\tdef {method.name}'

