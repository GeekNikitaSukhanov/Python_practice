'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'Дата: {self.day}-{self.month}-{self.year}'

    @classmethod
    def number(cls, day, month, year):
        cls.day = day
        cls.month = month
        cls.year = year
        day_number = int(cls.day)
        month_number = int(cls.month)
        year_number = int(cls.year)
        return f'Дата в формате числа: {day_number + month_number + year_number}'

    @staticmethod
    def validate(day, month, year):
        if day < 1 or day > 31:
            print(f'Ошибка ввода - число не может быть - {day} ')
        if month < 1 or month > 12:
            print(f'Ошибка ввода - месяц не может быть - {month}')

date_1 = Date(20, 2, 2021)
date_2 = Date(35, 2 , 2021)
date_3 = Date(23, 15, 2021)

print(date_1)
print(date_2)
print(date_3)
print(Date.number(20, 2, 2021))
Date.validate(35, 15, 2021)

