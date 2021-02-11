'''
Создать (программно) текстовый файл,
записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''
with open('Task_5.txt', 'w') as file:
    numbers = input('Введите любые числа через проблем ')
    file.write(numbers)

with open('Task_5.txt', 'r') as file:
    content = file.read().split()
    sum_numbers = 0
    for el in content:
        sum_numbers += int(el)
print(f'Сумма чисел, записанных в файл - {sum_numbers}')
