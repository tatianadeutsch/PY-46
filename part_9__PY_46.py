"""Реализуйте все возможные магические методы в классе Car.
"""

from part_4__PY__46 import MeansOfTransport


class Car(MeansOfTransport):
    airbags = 2
    _stereo_system = "Music plus"
    __park_asistent = "Control plus"
    car_drive = 4

    def __init__(self, color, brand, number_wheels, test_drive, prise_base_set=1000):
        super().__init__(color, brand)
        self.number_wheels = number_wheels
        self.mileage = 100
        self.wheel = 10
        self.prise_base_set = prise_base_set
        self.test_drive = list(test_drive)

    @classmethod
    def get_car_drive(cls):
        return cls.car_drive

    def __len__(self, *args):
        attrib = args[0]
        return len(attrib)

    def __add__(self, other):
        if type(other) != int:
            raise ArithmeticError("Операнд должен быть int")

        weight_auto = other + self.number_wheels * self.wheel
        return weight_auto

    def __eq__(self, other):
        return self.prise_base_set == other

    def __lt__(self, other):
        return self.prise_base_set < other.prise_base_set

    def __le__(self, other):
        return self.prise_base_set <= other.prise_base_set

    def __getitem__(self, item):
        return self.test_drive[item]

    def __setitem__(self, key, value):
        if key >= len(self.test_drive):
            off = key + 1 - len(self.test_drive)
            self.test_drive.extend([None] * off)
        self.test_drive[key] = value

    def __delitem__(self, key):
        del self.test_drive[key]

    def __hash__(self):
        return hash((self.prise_base_set, self.color, self.brand, self.number_wheels, self.prise_base_set))

    def __repr__(self):
        return (f"Мвшина оснащена подушками безопасности - {self.airbags} шт.,"
                f"аудиосистемой - {self._stereo_system}, "
                f"парковочным ассистентом - {self.__park_asistent}")

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


car_1 = Car('rosa', 'MB', 4, [10, 10, 9])
print("Вызов приводов через переменную класса: ", Car.car_drive)
print("Вызов приводов через экз. класса: " , car_1.get_car_drive())
print("Вызов приводов через обращ. к классу: ", Car.get_car_drive())
print(Car.__repr__)
print(f"Пакетов дополнительного оснащения: {car_1.__len__('TV', 'ABS')}")

print(f"Вес кузова с колесами составляет: {car_1.__add__(100)}")
print(car_1 + 150)
car_2 = Car('lila', 'Niva', 4, [9, 8, 9], 1200)

print('Цена равна: ', car_1 == car_2, car_1 == 1000)
print('Цена меньше: ', car_1 < car_2)
print('Цена больше или равна: ', car_2 <= car_1)
car_2[1]=10
print(f"Тест-драйв {car_2.brand} в аэродинамической трубе: {car_2.test_drive}")
# del car_1[1]

# # Создаем словарь и сравниваем хеши
print(hash(car_1))
print(hash(car_2))
d = {}
d[car_1] = 1
d[car_2] = 2
print(d)
print(car_1 == car_2)

