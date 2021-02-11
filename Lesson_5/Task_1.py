'''
Создать программный файл в текстовом формате
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
'''
input_list = []
while True:
    user_input = input('Введите любые данные или Enter для выхода')
    if user_input != '':
        input_list.append(user_input)
        with open('Task_1.txt', 'w') as file:
            for el in input_list:
                file.write(el + '\n')
    else:
        break



