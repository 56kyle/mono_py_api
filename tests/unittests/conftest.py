
import pytest
import os


@pytest.fixture(scope='session')
def unittest_directory(test_directory):
    return os.path.join(test_directory, 'unittests')


@pytest.fixture(scope='session')
def unittest_data(unittest_directory):
    return os.path.join(unittest_directory, 'data')








