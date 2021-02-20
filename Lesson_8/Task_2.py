'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class Myexception(Exception):
    def __init__(self,text):
        self.text = text


number_1 = int(input('Введите делимое число'))
number_2 = int(input('Введите делитель'))

try:
    if number_2 == 0:
        raise Myexception('Деление на ноль невозможно')
except Myexception as err:
    print(err)

else:
    result = number_1 / number_2
    print(f'Результат деления: {result}')



