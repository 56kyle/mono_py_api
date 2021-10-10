
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
        assert method.as_method() == f'\tdef {method.name}'


class TestMethodFunctions:
    def test_no_parameters_as_str(self):
        assert Method._parameters_as_str([]) == ''

    def test_simple_parameter_as_str(self):
        assert Method._parameters_as_str([Parameter(fragment='foo: System.Int32')]) == 'foo: System.Int32'

    def test_generic_parameter_as_str(self):
        assert Method._parameters_as_str([Parameter(fragment='foo: System.List<System.Int32>')]) == 'foo: System.List[System.Int32]'

    def test_multiple_simple_parameters_as_str(self):
        assert Method._parameters_as_str([
            Parameter(fragment='foo: System.Int32'),
            Parameter(fragment='foo: System.Boolean'),
            Parameter(fragment='foo: System.String')
        ]) == 'foo: System.Int32, foo: System.Boolean, foo: System.String'

    def test_multiple_generic_parameters_as_str(self):
        assert Method._parameters_as_str([
            Parameter(fragment='foo: System.List<System.Int32>'),
            Parameter(fragment='foo: System.Dictionary<System.String,System.List<System.Int32>>'),
            Parameter(fragment='foo: System.String')]) == 'foo: System.List[System.Int32], foo: System.Dictionary[System.String, System.List[System.Int32]], foo: System.String'
