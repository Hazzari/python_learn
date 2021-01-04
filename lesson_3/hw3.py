from typing import List

from utils import timing_dec


@timing_dec
def squares_of_numbers(*args, **kwargs):
    n = []
    if not kwargs:
        for x in args:
            n.append(x * x)
    else:
        if kwargs.get('square'):
            for x in args:
                n.append(x ** kwargs['square'])
        else:
            print(f"Неизвестный аргумент: {kwargs.popitem()[0]} \nпопробуйте передать: square")

    return n


@timing_dec
def filter_numbers(list_numbers: List, filter_criterion: int):
    result = ''

    if filter_criterion == 1:
        result = [x for x in list_numbers if not x % 2 and x != 0]
    elif filter_criterion == 2:
        result = [x for x in list_numbers if x % 2 and x != 0]
    elif filter_criterion == 3:
        def is_prime(n):
            if n % 2 == 0:
                return n == 2
            d = 3
            while d * d <= n and n % d != 0:
                d += 2
            return d * d > n

        result = [x for x in list_numbers if is_prime(x)]
        print(result)

    return result


def fib(level: int):
    f1, f2 = 1, 1
    count = 0
    print(0)
    print(1)
    while count < level:
        print(f2)
        next_f2 = f1 + f2
        next_f1 = f2
        f1, f2 = next_f1, next_f2
        count += 1


def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n=n - 1)
    return n * factorial_n_minus_1


if __name__ == '__main__':
    # f = squares_of_numbers(10, 11, 12, 13, 14, 15, 16, square=4)
    # print(f)

    # a = filter_numbers([x for x in range(100)], filter_criterion=2)
    # print(a)
    fib(10)
    print(factorial(9))
