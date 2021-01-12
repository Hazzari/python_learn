from abc import ABC
from dataclasses import dataclass

from food import Food
from my_exception import PositiveIntegerError


@dataclass
class Animal(ABC):
    name: str


@dataclass
class Bear(Animal):
    food: Food
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise PositiveIntegerError(self.age)
