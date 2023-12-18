"""Реализуйте абстрактный класс Animals,
создайте класс Cat, котрый будет наследоваться
от класса Animals }}и реализуйте метод {{voice.
"""

from abc import ABC, abstractmethod

class Animals(ABC):
    @abstractmethod
    def voice(self):
        pass

    @abstractmethod
    def __str__(self):
        print("Зверушки имеют национальность!")


class Cat(Animals):
    speak = "очень непонятно"
    @property
    def voice(self):
        super().voice()
        return f"Эта кошка говорит {self.speak}."

    @voice.setter
    def voice(self, speak):
        self.speak = speak

    def __str__(self):
        super().__str__()
        return "И даже кошки!"


cat_1 = Cat()
cat_2 = Cat()
print(cat_1)
print(cat_1.voice)
cat_1.speak = "мяв"
print(cat_1.voice)
cat_2.speak = "мяу"
print(cat_2.voice)
print(cat_1.__dict__)
print(cat_2.__dict__)

