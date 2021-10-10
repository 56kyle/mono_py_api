
import pytest

from src.parameter import Parameter


class TestParameter:
    @pytest.fixture
    def parameter(self) -> Parameter:
        return Parameter(fragment='__value: System.Collections.Generic.Dictionary<System.String,System.Collections.Generic.Dictionary<System.String,System.Boolean>>')

    def test_parameter_name(self, parameter: Parameter):
        assert parameter.name == '__value'

    def test_parameter_return_type(self, parameter: Parameter):
        assert str(parameter.return_type) == 'System.Collections.Generic.Dictionary[System.String, System.Collections.Generic.Dictionary[System.String, System.Boolean]]'

    def test_parameter_str(self, parameter: Parameter):
        assert str(parameter) == '__value: System.Collections.Generic.Dictionary[System.String, System.Collections.Generic.Dictionary[System.String, System.Boolean]]'






