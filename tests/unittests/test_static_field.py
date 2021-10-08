
import pytest
from src.static_field import StaticField


class TestStaticField:
    def test_simple_static_field(self):
        StaticField(line='\t\t\t\t10 : dimensions (type: System.Int32)\n')

    def test_static_field_with_generic_type(self):
        StaticField(line='\t\t\t\t0 : Item1 (type: T1)\n')

    def test_static_field_with_type_containing_generic(self):
        StaticField(line='\t\t\t\t18 : values (type: System.Object[])\n')


class TestStaticFieldMixins:
    @pytest.fixture(scope='class')
    def static_field(self):
        return StaticField(line='\t\t\t\t8 : encoders (type: System.Collections.Generic.Dictionary<System.Int32,Assets.Scripts.Unity.Network.Btd6MessageEncoder>)\n')

    def test_static_field_is_memorable(self, static_field: StaticField):
        assert static_field.address == '8'

    def test_static_field_is_parseable(self, static_field: StaticField):
        assert static_field.line == '\t\t\t\t8 : encoders (type: System.Collections.Generic.Dictionary<System.Int32,Assets.Scripts.Unity.Network.Btd6MessageEncoder>)\n'
        assert static_field.lines is None
        assert static_field.as_line() == '\tencoders: System.Collections.Generic.Dictionary[System.Int32, Assets.Scripts.Unity.Network.Btd6MessageEncoder]'


