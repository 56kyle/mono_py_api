
import pytest
from src.method import Method
from src.parameter import Parameter


class TestMethodMixins:
    @pytest.fixture(scope='class')
    def method(self):
        return Method(line='\t\t\t\t24b67a72990 : remove_ReconnectingEvent (value: System.Action<System.Collections.Generic.IEnumerable<System.Threading.Tasks.Task<System.Int32>>>) -> System.Void')

    def test_method_is_memorable(self, method: Method):
        assert method.address == '24b67a72990'

    def test_method_is_parseable(self, method: Method):
        assert method.line == '\t\t\t\t24b67a72990 : remove_ReconnectingEvent (value: System.Action<System.Collections.Generic.IEnumerable<System.Threading.Tasks.Task<System.Int32>>>) -> System.Void'
        assert method.lines is None
        assert method.as_method() == f'\tdef remove_ReconnectingEvent(self, value: System.Action[System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task[System.Int32]]]) -> System.Void:\n\t\tpass'


class TestMethodFunctions:
    def test_no_parameters_as_str(self):
        assert Method._parameters_as_str([]) == 'self'

    def test_simple_parameter_as_str(self):
        assert Method._parameters_as_str([Parameter(fragment='foo: System.Int32')]) == 'self, foo: System.Int32'

    def test_generic_parameter_as_str(self):
        assert Method._parameters_as_str([Parameter(fragment='foo: System.List<System.Int32>')]) == 'self, foo: System.List[System.Int32]'

    def test_multiple_simple_parameters_as_str(self):
        assert Method._parameters_as_str([
            Parameter(fragment='foo: System.Int32'),
            Parameter(fragment='foo: System.Boolean'),
            Parameter(fragment='foo: System.String')
        ]) == 'self, foo: System.Int32, foo: System.Boolean, foo: System.String'

    def test_multiple_compound_parameters_as_str(self):
        assert Method._parameters_as_str([
            Parameter(fragment='foo: System.Numbers.Int32'),
            Parameter(fragment='bar: System.Values.Boolean'),
            Parameter(fragment='baz: System.Collections.Enumerable.Dictionary')
        ]) == 'self, foo: System.Numbers.Int32, bar: System.Values.Boolean, baz: System.Collections.Enumerable.Dictionary'

    def test_multiple_generic_parameters_as_str(self):
        assert Method._parameters_as_str([
            Parameter(fragment='foo: System.List<System.Int32>'),
            Parameter(fragment='foo: System.Dictionary<System.String,System.List<System.Int32>>'),
            Parameter(fragment='foo: System.String')]) == 'self, foo: System.List[System.Int32], foo: System.Dictionary[System.String, System.List[System.Int32]], foo: System.String'
