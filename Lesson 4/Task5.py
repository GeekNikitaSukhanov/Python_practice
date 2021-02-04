'''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''
from functools import reduce
def func(el, el_next):
    return el_next * el
lst = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(func, {el for el in lst}))

