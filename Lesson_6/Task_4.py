'''
Реализуйте базовый класс Car.
●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
'''


class Car:
    def __init__(self, name, color, speed, is_police=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина', {self.name}, 'поехала')

    def stop(self):
        print('Машина', {self.name}, 'остановилась')

    def turn(self):
        print('Машина', {self.name}, 'повернула')

    def show_speed(self):
        print(f'Скорость машины {self.name} - {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
        else:
            print(f'Скорость машины {self.name} - {self.speed}')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print(f'Скорость машины {self.name} - {self.speed}')


town_speed = int(input('Введите скорость машины в городе'))
town_car = TownCar('Тойота', 'Черная', town_speed)
print(f' Название машины - {town_car.name}')
print(f' Цвет машины - {town_car.color}')
town_car.show_speed()
town_car.go()
town_car.turn()
town_car.stop()

work_speed = int(input('Введите скорость рабочей машины'))
work_car = WorkCar('Сузуки', 'Красная', work_speed)
print(f' Название машины - {work_car.name}')
print(f' Цвет машины - {work_car.color}')
work_car.show_speed()
work_car.go()
work_car.turn()
work_car.stop()
