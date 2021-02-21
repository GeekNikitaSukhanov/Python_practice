'''
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''
# Не хватило времени, чтобы решить
'''
class Warehouse:
    def __init__(self, capacity):
        self.capacity = capacity

    def __str__(self):
        print f'Склад вместимостью {capacity} едииниц техники'

    def check_capacity(self):
        if self.capacity > 10:
            print(f'Склад переполнен')



class Office_supplies(Warehouse):
    def __init__(self, capacity, producer, price, type):
        super().__init__(capacity)
        self.producer = producer
        self.price = price
        self.type = type
        self.info = {Единиц техники}


class Computer:
    def __init__(self, producer, price, type, processor):
        super().__init__(producer, price, type)
        self.processor = processor

    def delivery(self):
        self.capacity = 1
        print(f'{self.type} {self.producer} передано на склад')
        return self.capacity

class Printer:
    def __init__(self, producer, price, type, ink):
        super().__init__(producer, price, type)
        self.ink = ink


class Scanner:
    def __init__(self, producer, price, type, resolution):
        super().__init__(producer, price, type)
        self.resolution = resolution
'''
