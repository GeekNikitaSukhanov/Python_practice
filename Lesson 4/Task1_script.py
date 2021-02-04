'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
'''
from sys import argv

script_name, hours_worked, hour_rate, bonus_rate = argv
salary = int(hours_worked) * 20 * int(hour_rate)
annual_salary = salary * 12
bonus = int(bonus_rate) / 100
annual_bonus = annual_salary * bonus
total_comp = annual_salary + annual_bonus

print('Зарплата в месяц', salary)
print('Вознаграждение в год', annual_salary)
print('Годовая премия', annual_bonus)
print('Итого вознаграждение в год', total_comp)
