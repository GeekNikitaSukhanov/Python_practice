'''
Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч,
вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32
'''
from typing import Dict, Any

file = open('Task_3.txt', 'w')
salary_list = []
employee_list = []
count_rows = 0
salary_sum = 0
while count_rows < 10:
    employee_info = input('Введите имя и оклад сотрудника (не менее 10) или enter для выхода ')
    if employee_info != '':
        file.write(employee_info + '\n')
        count_rows += 1
    else:
        break
file.close()
with open('Task_3.txt', 'r') as file:
    content = file.read().split('\n')
    content.remove('')
    for el in content:
        new_list = el.split()
        salary_sum += int(new_list[1])
        if int(new_list [1]) > 20000:
            employee_list.append(new_list[0])
print(f'Сотрудники с окладом свышен 20 тыс руб - {employee_list}')
average_salary = salary_sum / count_rows
print(f'Средний оклад по сотрудникам - {average_salary}')
file.close()





