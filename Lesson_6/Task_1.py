'''
Создать класс TrafficLight (светофор).

●	определить у него один атрибут color (цвет) и метод running (запуск);
●	атрибут реализовать как приватный;
●	в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
●	продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
●	переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
●	проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
class TrafficLight:
    __color = 'Black'
    def running(self, button):
        time = 0
        if button == 'start':
            while time < 7:
                print('Красный сигнал светофора')
                time += 1
                print(f'Отсчет времени - {time} сек')
                while time >= 7 and time < 9:
                    print('Желтый сигнал светофора')
                    time = time + 1
                    print(f'Отсчет времени - {time} сек')
                    while time >=9 and time <11:
                        print('Зеленый сегнал светофора')
                        time = time + 1
                        print(f'Отсчет времени - {time} сек')
                        if time == 11:
                            time = time - 11
                            button = input('Продолжить? ')
                            if button == '':
                                pass
                            else:
                                time = 12
                                print('Работа светофора завершена ')

button = input('Type start to turn traffic lights or cancel to cancel ')
if button == 'cancel':
    print('You canceled the start of traffic lights')
else:
    a = TrafficLight()
    a.running(button)
