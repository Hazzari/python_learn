from animals import Bear
from zoo import Zoo
from food import Food

food = Food('Мед', 'Сладкое')
bear = Bear('Faust', food=food, age=5)
zoo = Zoo()

zoo.animals.append(bear)

print(zoo.animals)
print(zoo)
