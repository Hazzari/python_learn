from dataclasses import dataclass, field
from typing import Any, List


@dataclass()
class Node:
    _value: int
    _children: list = field(default_factory=list)

    # def __repr__(self):
    #     return f'Node({self._value!r})'

    def add_childcren(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):

        yield self
        for c in self:
            # yield from c.depth_first()
            for x in c.depth_first():
                yield x


if __name__ == '__main__':
    root = Node(0)
    children1 = Node(1)
    children2 = Node(2)

    root.add_children(children1)
    root.add_children(children2)

    # print(root._children[1]._value)
    # print(root._children)
    # print()

    children1.add_children(Node(3))
    children1.add_children(Node(4))
    children2.add_children(Node(5))
    #
    # print(children1._children)
    # print(children2._children)

    for ch in reversed(root.depth_first()):
        print(ch)

#
# some_list1 = [x for x in range(5)]
# some_list2 = [x for x in range(5, 10)]
#
# print(some_list1)
# print(some_list2)
#
#
# def some_func(some_list: list) -> None:
#
#
#     pass
