
from src.typelike import Typelike


class TestTypelike:
    def test_typelike_find_one_generic(self):
        assert str(Typelike(fragment='System.Action<System.Int32>')) == 'System.Action[System.Int32]'

    def test_typelike_find_nested_generic(self):
        assert str(Typelike(fragment='System.Action<System.Collections.Generic.IEnumerable<System.Threading.Tasks.Task>>')) == 'System.Action[System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task]]'

    def test_typelike_find_multiple_generics(self):
        assert str(Typelike(fragment='System.Action<System.Collections.Generic.IEnumerable,System.Threading.Tasks.Task<System.Int32>>')) == 'System.Action[System.Collections.Generic.IEnumerable, System.Threading.Tasks.Task[System.Int32]]'
