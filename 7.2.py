'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod

class Dress(ABC):

    def __init__(self, parameters):
        self.parameters = parameters

    def __add__(self, other):
        return self.parameters + other.parameters

    @abstractmethod
    def expense_textile(self):
        pass

class Coat(Dress):
    @property
    def expense_textile(self):
        return round(self.parameters / 6.5 + 0.5)

    def __str__(self):
        return str(self.expense_textile)


class Suit(Dress):
    @property
    def expense_textile(self):
        return round(2 * self.parameters + 0.3)

    def __str__(self):
        return str(self.expense_textile)

a = Coat(16)
print('Затраты ткани на пиджак:', a)

b = Suit(16)
print('Затраты ткани на костюм:', b)

print('Общие затраты ткани:', a + b) # не понял почему считает не правильно( перевод в int не дал результа)