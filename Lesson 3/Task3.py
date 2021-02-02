'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(a, b, c):
    max_el = max(a, b, c)
    min_el = min(a, b, c)
    list = [a, b, c]
    for el in list:
        if el != max_el and min_el:
            mid_el = el
    return max_el + mid_el
'''Не смог понять, почему выдает ошибку, если в return ввести функцию sum'''
first = int(input('Введите число 1 '))
second = int(input('Введите число 2 '))
third = int(input('Введите число 3 '))
result = my_func(first, second, third)
print(f'Сумма двух наибольших чисел из трех: {result}')
