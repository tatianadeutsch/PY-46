"""В классе Car добавьте переменную класса
car_drive = 4 и реализуйте classmethod,
который выводит на экран переменную car_drive
"""

from part_4__PY__46 import MeansOfTransport


class Car(MeansOfTransport):
    car_drive = 4

    def __init__(self, color, brand, number_wheels):
        super().__init__(color, brand)
        self.number_wheels = number_wheels

    @classmethod
    def get_car_drive(cls):
        return cls.car_drive

    def __str__(self):
        return super().__str__() + ', ' + (f' количество колес - {self.number_wheels}, '
                                           f'количество приводов - {self.car_drive}')


class Moped(MeansOfTransport):
    def __init__(self, color, brand, number_wheels):
        super().__init__(color, brand)
        self.number_wheels = number_wheels

    @staticmethod
    def s_v_t(s, max_v):
        t = s / max_v
        return t


car_1 = Car('rosa', 'MB', 4)
print("Вызов приводов через переменную класса: ", Car.car_drive)
print("Вызов приводов через экз. класса: " ,car_1.get_car_drive())
print("Вызов приводов через обращ. к классу: ", Car.get_car_drive())
print(car_1)







