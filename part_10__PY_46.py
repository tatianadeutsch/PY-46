"""Реализуйте класс Calculator, в котором
будет один метод, для вычисления
суммы двух чисел.
"""

class Calculator:
    def sum(self, x, y):
        if type(x) != int or type(y) != int:
            raise TypeError('Данные должны быть числом')
        return x + y


calc_1 = Calculator()
calc_2 = Calculator()
print(calc_1.sum(100, 200))
print(calc_2.sum(-111, -111))
# print(calc_2.sum("-111", -111))


"""Реализуйте еще один класс, который будет
наследоваться от класса Calculator
и перегрузите метод для вычисления
суммы двух чисел, чтобы он делал конкатенацию двух строк.
"""

class Concatenation(Calculator):
    def sum(self, x, y):
        if type(x) != str or type(y) != str:
            raise TypeError('Данные должны быть строкой')
        return x*2 + y


cont_1 = Concatenation()
cont_2 = Concatenation()
print(cont_1.sum("Ура! ", "Зима пришла!! "))
# print(cont_1.sum(2, 2))
