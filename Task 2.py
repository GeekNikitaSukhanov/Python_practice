'''
Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''
a = input("Введите элементы вашего списка через пробел ")
list_1 = list(a)
b = " "
for el in list_1:
    if el is b:
        list_1.remove(el)
c = list_1.count(el)
if c % 2 == 0:
    for el in list_1:
        position = list_1.index(el)
        next_position = position + 1
        if position % 2 == 0:
            list_1.pop(position)
            list_1.insert(next_position,el)
else:
    for el in list_1:
        position = list_1.index(el)
        next_position = position + 1
        while position < c:
            if position % 2 == 0:
                list_1.pop(position)
                list_1.insert(next_position,el)
print(list_1)

        





