# from unittest import TestCase
from .solver import mul, sub, SUB_ERRORS_TEXT
from pytest import mark, raises

# #  Unittest
# class TestSolver(TestCase):
#     def test_add(self):
#         res = Solver.add(1, 2)
#         self.assertEqual(res, 3)
#
#         res = Solver.add(4, 5)
#         self.assertEqual(res, 9)
#
#     def test(self):
#         pass
param_list = [
    ((3, 5), 15),
    ((1, 10), 10),
    ((4, 0), 0),
    ((4, 0), 1),
    ((4, 8), 32),
]


# Параметризация тестов, передаем разные значения для тестов
@mark.parametrize(
    # Называем переменные через которые будут передаваться -
    # параметры в функцию

    "values, expected_result",
    # передаем список tuple ((value), expected_result)
    param_list,
)
def test_mul(values, expected_result):
    res = mul(*values)
    assert res == expected_result


def test_sub_raises():
    with raises(TypeError) as exc_info:
        sub(1, '')

    assert str(exc_info.value) == SUB_ERRORS_TEXT
