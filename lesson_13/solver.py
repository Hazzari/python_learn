class Solver:
    @classmethod
    def add(cls, a, b):
        res = a + b
        return res


def mul(a, b):
    return a * b


SUB_ERRORS_TEXT = 'All arguments have to be int or float'


def sub(a, b):
    if not all(
            map(
                lambda v: isinstance(v, (int, float)),
                (a, b),
            )
    ):
        raise TypeError(SUB_ERRORS_TEXT)
    return a - b
