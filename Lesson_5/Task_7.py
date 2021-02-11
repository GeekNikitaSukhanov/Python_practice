'''
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''
import json
with open('Task_7.txt', 'w') as file:
    print('Нажмите Enter для выхода либо введите следующие параметры фирм: ')
    while True:
        file_input = input('Введите название фирмы, форму собственности, выручку и издержки через пробел ')
        if file_input == '':
            print('Выход из программы')
            break
        else:
           file.write(file_input + '\n')
firm_dict = {}
average_dict ={}
final_list = []
firm_count = 0
sum_profit = 0
with open('Task_7.txt', 'r') as file:
    for line in file:
        firm_name = line.split()[0]
        firm_incorp = line.split()[1]
        firm_revenue = int(line.split()[2])
        firm_cost = int(line.split()[3])
        firm_profit = firm_revenue - firm_cost
        firm_dict[firm_name] = firm_profit
        if firm_profit > 0:
            sum_profit += firm_profit
            firm_count += 1
        average_profit = sum_profit / firm_count
        average_dict['Средняя прибыль'] = average_profit
    final_list.append(firm_dict)
    final_list.append(average_dict)
    print(final_list)

with open('Task_7.txt', 'w') as file:
    json.dump(final_list,file)


