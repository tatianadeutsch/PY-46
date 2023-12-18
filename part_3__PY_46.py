"""Создайте класс {{MeansOfTransport }}(для определения цвета и марки машины),
принимающий 2 аргумента при инициализации (марка и цвет транспортного стредства).
В этом классе реализуйте методы show_color(), выводящий на печать
цвет транспортного средства и show_brand, для получения марки транспортного средства.
"""

class MeansOfTransport:
    'Определяет цвет и марку машины'
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_color(self):
        print(self.color)

    def show_brand(self):
        return self.brand

auto_1 = MeansOfTransport('Audi', 'red')
auto_1.show_color()
print(auto_1.brand)
print(auto_1.__dict__)

auto_2 = MeansOfTransport('VW', 'metallic')
auto_2.show_color()
print(auto_2.brand)
print(auto_2.__dict__)

