
from src.dll import Dll
from src.klass import Klass
from src.field import Field
from src.static_field import StaticField
from src.method import Method
from src.game import Game


if __name__ == '__main__':
    with open('../bloons_auto/api_creation/gen/data/cheat_engine_direct_no_delegates_pruned.py', 'r') as file:
        game = Game(lines=file.readlines())
        for dll in game.dlls:
            dll.gen_api()

