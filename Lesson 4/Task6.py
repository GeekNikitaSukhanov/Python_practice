'''
Реализовать два небольших скрипта:
●	итератор, генерирующий целые числа, начиная с указанного;
●	итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3.
При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие,
при котором повторение элементов списка прекратится.
'''
from itertools import count, cycle
a = int(input('Укажите, с какого числа начать генерацию чисел -'))
print('Генерация чисел с указанного вами')
for el in count(a):
    if el > 30:
        break
    else:
        print(el)

b = input('Введите любые элементы через пробел ').split()
counter = 0
print('Повторение ваших элементов до 30 раз')

for el in cycle(b):
    if counter > 30:
        break
    else:
        print(el)
        counter += 1

