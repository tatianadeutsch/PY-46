"""Реализуйте два класса Car и Moped, которые будут
наследоваться от класса MeansOfTransport.
При инициализации они должны принимать новый аргументы(количество колес).
"""

from part_4__PY__46 import MeansOfTransport


class Car(MeansOfTransport):
    def __init__(self, color, brand, number_wheels):
        self.number_wheels = number_wheels
        super().__init__(color, brand)

    def __str__(self):
        return super().__str__() + ', ' + f' количество колес - {self.number_wheels}'

class Moped(MeansOfTransport):
    def __init__(self, color, brand, number_wheels):
        self.number_wheels = number_wheels
        super().__init__(color, brand)


car_1 = Car('rosa', 'MB', 4)
print(car_1.__dict__)
car_1.number_wheels = 6
print(car_1, "\n")

car_1 = Moped('lily', 'HL', 2)
print(car_1.__dict__)
car_1.number_wheels = 3
print(car_1, "\n")






