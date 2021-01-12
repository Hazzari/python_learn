class PositiveIntegerError(ValueError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Возраст не может быть отрицательным. Вы ввели {self.value}'
