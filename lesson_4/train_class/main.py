from car import PassengerCar
from lesson_4 import Motor

v6 = Motor('v6', 6, 12, 9, 12)

my_car = PassengerCar(_model='BMW X6', _long=3, _carrying_capacity=400, _max_speed=310, _weight=1600, motor=v6)

print(my_car.model)


