'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod


class Clothes (ABC):
    def __init__(self):
        @abstractmethod
        def material(self):
            pass


class Coat(Clothes):
    def __init__(self, v):
        super().__init__()
        self.v = v

    @property
    def material(self):
        material = self.v / 6.5 + 0.5
        return material

    @material.setter
    def limit(self, v):
        if v > 100:
            print('Такого размера нет, берем максимальный - 60')
            self.v = 60
        elif v < 0:
            print('Берем минимальный размер - 5')
            self.v = 5
        else:
            self.v = v

class Suit(Clothes):
    def __init__(self, h):
        super().__init__()
        self.h = h
    def material(self):
        material = self.h * 2 + 0.3
        return material

coat = Coat(6.5)
suit = Suit(10)
print(coat.material)
print(suit.material())
all_material = float(coat.material) + float(suit.material())
print(f'Общий расход ткани - {all_material}')