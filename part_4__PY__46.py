"""Работаем с классом из 3 пункта.
Реализуйте сеттеры и геттеры для цвета и марки транспортного средства.
"""

class MeansOfTransport:
    'Возращает и присваивает цвет и марку машины'
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    @classmethod
    def verify_color(cls, color):
        if type(color) != str:
           raise TypeError("Значение color должно быть строкой")

    @classmethod
    def verify_brand(cls, brand):
        if type(brand) != str:
            raise TypeError("Значение brand должно быть строкой")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self.verify_color(color)
        self._color = color

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self.verify_brand(brand)
        self._brand = brand

    def __str__(self):
        return f'{self._brand}, {self._color}'


auto_1 = MeansOfTransport('red', 'Audi')
# print(auto_1)
# print(auto_1.color)
# auto_1.color = 'orange'
# print(auto_1.color)
# print(auto_1.__dict__, "\n")
#
# auto_2 = MeansOfTransport('metallic', 'VW')
# print(auto_2)
# print(auto_2.brand)
# auto_2.brand = 'Porsche'
# print(auto_2.brand)
# print(auto_2.__dict__, "\n")





