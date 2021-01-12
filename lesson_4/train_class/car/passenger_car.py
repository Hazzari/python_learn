from dataclasses import dataclass, field
from .base_car import Car
from lesson_4 import Motor


@dataclass
class PassengerCar(Car):
    motor: Motor = field(default_factory=Motor)

    def speed_up(self):

        if self._speed < self._max_speed:
            self._speed += 1
            print(f'Прибавляем скорость до {self._speed}')
        else:
            print(f'Ускорение невозможно, скорость максимальна')

    def speed_down(self):
        if self._speed > 0:
            self._speed -= 1
            print(f'Сбавляем скорость до {self._speed}')

    def stop(self):
        for x in range(self._speed, 0, -5):
            self._speed -= 5
            if self._speed < 0:
                self._speed = 0
            print(f'Тормозим! Скорость = {self._speed}')

        print(f'Скорость = {self._speed}')

    @property
    def my_speed(self):
        return self._speed

    @property
    def make_sound(self):
        return f'{self._sound}'
