from random import randint

import pytest


@pytest.fixture(params=[(randint(0,100), randint(0,100))])
def first_fixture(request):
    print("\nПечать из: 'Первая фикстура'")
    return request.param


def test_one(first_fixture):
    print(f'Печать из тестовой функции и возвращаемое значение {first_fixture}')


def test_two(first_fixture):
    pass


class TestFunction:

    def test_from_test_class_one(self, first_fixture):
        pass

    def test_from_test_class_two(self, first_fixture):
        pass
