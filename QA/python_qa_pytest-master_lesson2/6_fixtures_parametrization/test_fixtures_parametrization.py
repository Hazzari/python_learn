import pytest


@pytest.mark.parametrize("test_input", [1, 2, 3])
def test_one_2(test_input):
    print(test_input)


@pytest.mark.parametrize("test_input", ['a', 'b', 'c'])
class TestClassParametrized:

    # Все функци должны использовать аргумент
    def test_one(self, test_input): ...

    def test_two(self, test_input): ...


# Parametrize with fixture
#
# def test_one_1(fixture_with_params):
#     print(fixture_with_params)
#
# Combine parametrization
#
@pytest.mark.parametrize("test_input", [1, 2, 3])
def test_one_2(test_input, fixture_with_params):
    print()
    print(test_input)
    print(fixture_with_params)
