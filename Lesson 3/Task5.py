'''
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
'''
def func():
    stop = False
    sum_1 = 0
    sum_2 = 0
    sum_all = 0
    while stop is False:
        a = input('Введите строку чисел через пробел ').split()
        a_list = [item for item in a]
        for el in a_list:
            if el == 'q' or el == 'Q':
                a_list.remove(el)
                a_list_number = [int(item) for item in a_list]
                sum_2 = sum(a_list_number)
                print(f'Выход из программы')
                stop = True
                break
        else:
            b_list_number = [int(item) for item in a_list]
            calc = sum(b_list_number)
            sum_1 = sum_1 + calc
            print(f'Сумма введенных числе - {sum_1}')
            print('Продолжайте ввод числе или нажмите Q для выхода')
    sum_all = sum_all + sum_1 + sum_2
    return sum_all
result = func()
print(f'Сумма всех введенных числе - {result}')