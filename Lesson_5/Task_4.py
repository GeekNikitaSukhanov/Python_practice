'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
file = open('Task_4.txt', 'w')
file_input = ['One - 1\n', 'Two - 2\n', 'Three - 3\n', 'Four - 4\n']
file.writelines(file_input)
file.close()
russian_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
number = []
count = 1
russian_list = []
with open('Task_4.txt', 'r') as file:
    content = file.read().split('\n')
    content.remove('')
    english_keys = russian_dict.keys()
    for el in content:
        new_el = el.split()[0]
        russian_el = russian_dict.get(new_el)
        russian_string = el.replace(new_el,russian_el)
        russian_list.append(russian_string)

with open('Task4_result.txt', 'w') as file:
    for el in russian_list:
        file.write(el + '\n')








