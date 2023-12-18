"""В классе {{Moped}}напишите статическую функцию,
которая на вход будет принимать расстояние
и максимальную скорость, а на выходе получать время,
за которое проедет мопед это расстояние.
"""

from part_4__PY__46 import MeansOfTransport


class Car(MeansOfTransport):
    def __init__(self, color, brand, number_wheels):
        super().__init__(color, brand)
        self.number_wheels = number_wheels

    def __str__(self):
        return super().__str__() + ', ' + f' количество колес - {self.number_wheels}'


class Moped(MeansOfTransport):
    def __init__(self, color, brand, number_wheels):
        super().__init__(color, brand)
        self.number_wheels = number_wheels

    @staticmethod
    def s_v_t(s, max_v):
        t = s / max_v
        return t


car_1 = Car('rosa', 'MB', 4)
print(car_1.__dict__)
car_1.number_wheels = 6
print(car_1, "\n")

moped_1 = Moped('lily', 'HL', 2)
print(moped_1.__dict__)
moped_1.number_wheels = 3
print(moped_1, "\n")

moped_1.s_v_t(100, 60)
print(f"Время в пути на мопеде {moped_1} составит {Moped.s_v_t(80, 50)} ч")
