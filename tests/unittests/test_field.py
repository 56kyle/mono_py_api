
import pytest
from src.field import Field


class TestField:
    def test_simple_field(self):
        Field(line='\t\t\t\t10 : dimensions (type: System.Int32)\n')

    def test_field_with_generic_type(self):
        Field(line='\t\t\t\t0 : Item1 (type: T1)\n')

    def test_field_with_type_containing_generic(self):
        Field(line='\t\t\t\t18 : values (type: System.Object[])\n')


class TestFieldMixins:
    @pytest.fixture(scope='class')
    def field(self):
        return Field(line='\t\t\t\t10 : dimensions (type: System.Object[])\n')

    def test_field_is_memorable(self, field: Field):
        assert field.address == '10'

    def test_field_is_parseable(self, field: Field):
        assert field.line == '\t\t\t\t10 : dimensions (type: System.Object[])\n'
        assert field.lines is None
        assert field.as_line() == '\t\tself.dimensions: List[System.Object] = dimensions'


