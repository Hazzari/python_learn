import pytest
import logging

logging.basicConfig()
@pytest.fixture
def list_fixture():
    return 6


def test_list(list_fixture):
    print()
    my_list = [x for x in range(list_fixture)]
    print(type(my_list))
    assert len(my_list)==list_fixture, 'hhhh'
