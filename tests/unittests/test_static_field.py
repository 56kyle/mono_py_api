
import pytest
from src.static_field import StaticField


class TestStaticFieldMixins:
    @pytest.fixture(scope='class')
    def static_field(self):
        return StaticField(line='\t\t\t\t8 : encoders (type: System.Collections.Generic.Dictionary<System.Int32,Assets.Scripts.Unity.Network.Btd6MessageEncoder>)\n')

    def test_static_field_is_memorable(self, static_field: StaticField):
        assert static_field.address == '8'

    def test_static_field_is_parseable(self, static_field: StaticField):
        assert static_field.line == '\t\t\t\t8 : encoders (type: System.Collections.Generic.Dictionary<System.Int32,Assets.Scripts.Unity.Network.Btd6MessageEncoder>)\n'
        assert static_field.lines is None
        assert static_field.as_class_variable() == '\tencoders: System.Collections.Generic.Dictionary[System.Int32, Assets.Scripts.Unity.Network.Btd6MessageEncoder]'
        print(static_field.as_class_method())
        assert static_field.as_class_method() == '\t@classmethod\n\tdef encoders(cls) -> System.Collections.Generic.Dictionary[System.Int32, Assets.Scripts.Unity.Network.Btd6MessageEncoder]:\n\t\tpass'


