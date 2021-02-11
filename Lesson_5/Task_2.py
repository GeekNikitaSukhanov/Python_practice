'''
Создать текстовый файл (не программно), сохранить в нём несколько строк
выполнить подсчёт строк и слов в каждой строке.
'''
file = open('Task_2.txt', 'w')
input_list = []
count_lines = 0
count_words = 0
while True:
    user_input = input('Введите любые данные или нажмите Enter для выхода ')
    if user_input != '':
        file.write(user_input + '\n')
    else:
        break
file.close()
file = open('Task_2.txt', 'r')
for line in file:
    count_lines += 1
    count_words = count_lines + line.count(' ')

print(f'Число строк в файле - {count_lines}')
print(f'Число слов в файле - {count_words}')
file.close()


