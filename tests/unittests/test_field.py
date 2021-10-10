
import pytest
from src.field import Field
from src.typelike import Typelike


class TestFieldMixins:
    @pytest.fixture(scope='class')
    def field(self):
        return Field(line='\t\t\t\t10 : dimensions (type: System.Object[])\n')

    def test_field_is_memorable(self, field: Field):
        assert field.address == '10'

    def test_field_is_parseable(self, field: Field):
        assert field.line == '\t\t\t\t10 : dimensions (type: System.Object[])\n'
        assert field.lines is None
        assert field.as_instance_variable() == '\t\tself.dimensions: list[System.Object] = dimensions'


class TestFieldMethods:

    def test_as_instance_variable_simple(self):
        assert Field._as_instance_variable(name='value', return_type='System.Int32') == '\t\tself.value: System.Int32 = value'

    def test_as_instance_variable_complex(self):
        assert Field._as_instance_variable(name='__value', return_type=Typelike(fragment='System.Collections.Dictionary<System.String,System.List<System.Int32>>')) == '\t\tself.__value: System.Collections.Dictionary[System.String, System.List[System.Int32]] = __value'





