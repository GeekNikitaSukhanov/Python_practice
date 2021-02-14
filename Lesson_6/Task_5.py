'''
Реализовать класс Stationery (канцелярская принадлежность).

●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print(f'Инструментом {self.title} - отрисовка тонкой линеей')


class Pencil(Stationary):
    def draw(self):
        print(f'Инструментом {self.title} - отрисовка стираемой линеей')


class Marker(Stationary):
    def draw(self):
        print(f'Инструментом {self.title} - отрисовка жирной линеей')


pen = Pen('Ручка Erik Krauze')
print(f'Название инструмента - {pen.title}')
pen.draw()

pencil = Pencil('Карандаш kohinoor')
print(f'Название инструмента - {pencil.title}')
pencil.draw()

marker = Marker('Маркер sharpie')
print(f'Название инструмента - {marker.title}')
marker.draw()
