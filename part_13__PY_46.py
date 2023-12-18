"""Реализуйте класс Dog. Придумайте,
какие переменные
будет принимать данный класс и
какие методы будут реализованы.
Реализуйте в этом классе паттерн Singleton
"""


class Dog:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name, breed, age, medal=0):
        self.name = name
        self.breed = breed
        self.age = age
        self.medal = medal

    def get_feed(self):
        return f'{self.breed} {self.name} есть только корм "Элит"'

    def get_show(self):
        return f'Выставка собак породы {self.breed} возрастом {self.age} год(лет) пройдет в декабре.'

    def __str__(self):
        return f'{self.breed} {self.name} имеет {self.medal} медалей'


dog_1 = Dog("Бруно", "Водолаз", 4, 3)
print(dog_1)
print(dog_1.get_feed())

dog_2 = Dog("Фагот", "Терьер", 1)
print(dog_2)
print(dog_1.get_show())
print(id(dog_1), id(dog_2))
print(dog_1.__dict__)
print(dog_2.__dict__)


