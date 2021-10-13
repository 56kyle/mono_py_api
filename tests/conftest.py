
import pytest
import os


@pytest.fixture(scope='session')
def test_directory():
    return os.path.join(os.getcwd().split('tests')[0], 'tests')

