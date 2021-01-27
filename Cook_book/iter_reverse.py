from dataclasses import dataclass


@dataclass
class Counter:
    start: int

    # прямой итератор
    def __iter__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

    # обратный итератор
    def __reversed__(self):

        n = self.start
        while n > 0:
            yield n
            n -= 1


if __name__ == '__main__':
    some_class = Counter(10)

    for x in reversed(some_class):
        print(x)

    print()
    print('*' * 2)
    print()

    for x in some_class:
        print(x)
