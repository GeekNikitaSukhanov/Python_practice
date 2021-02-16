'''
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31	22
37	43
51	86

3	5	32
2	4	6
-1	64	-8

3	5	8	3
8	3	7	1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''


class Matrix:
    def __init__(self, list_1, list_2, list_3):
        self.list_1 = list_1
        self.list_2 = list_2
        self.list_3 = list_3

    def __str__(self):
        return f' {self.list_1}\n {self.list_2}\n {self.list_3}'

    def __add__(self, other):
        i = 0
        new_list_1 = []
        while i < len(self.list_1):
            new_list_1.append(self.list_1[i] + other.list_1[i])
            i += 1
        i = 0
        new_list_2 = []
        while i < len(self.list_2):
            new_list_2.append(self.list_2[i] + other.list_2[i])
            i += 1
        i = 0
        new_list_3 = []
        while i < len(self.list_3):
            new_list_3.append(self.list_3[i] + other.list_3[i])
            i += 1
        return Matrix(new_list_1, new_list_2, new_list_3)

list_1 = [1, 2, 3, 4]
list_2 = [2, 3, 4, 5]
list_3 = [3, 4, 5, 6]
list_1_other = [4, 5, 6, 7]
list_2_other = [5, 6, 7, 8]
list_3_other = [6, 7, 8, 9]
first_matrix = Matrix(list_1, list_2, list_3)
second_matrix = Matrix(list_1_other, list_2_other, list_3_other)
print(first_matrix + second_matrix)
