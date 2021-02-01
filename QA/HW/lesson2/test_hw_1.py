from random import randint

import pytest
from hw1 import addition



@pytest.fixture(params=[(randint(0, 100), randint(0, 100)) for x in range(10)])
def first_fixture(request):
    print("\nПечать из: 'Первая фикстура'")
    return request.param


def test_one(first_fixture):
    a = addition(param_one=first_fixture[0],
                 param_two=first_fixture[1])
    print(a)
