from dataclasses import dataclass

from lesson_4 import Vehicle


@dataclass
class Car(Vehicle):
    _wheels: int = 4
    _sound: str = 'Beep'
