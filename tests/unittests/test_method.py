
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
        return Method(line='\t\t\t\t10 : dimensions (type: System.Object[])\n')

    def test_method_is_memorable(self, method: Method):
        assert method.address == '10'

    def test_method_is_parseable(self, method: Method):
        assert method.line == '\t\t\t\t10 : dimensions (type: System.Object[])\n'
        assert method.lines is None
        assert method.as_line() == '\t\tself.dimensions: List[System.Object] = dimensions'

