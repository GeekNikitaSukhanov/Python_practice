'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

print("Решение через list")
list_seasons = ["Зима", "Весна", "Лето", "Осень"]
a = int(input("Введите номер месяца "))
if a < 3 or a == 12:
    print(list_seasons[0])
elif a > 2 and a < 6:
    print(list_seasons[1])
elif a > 5 and a < 9:
    print(list_seasons[2])
elif a > 8 and a < 12:
    print(list_seasons[3])

print("Решение через dict")
seasons = {1: "Зима", 2: "Весна", 3: "Лето", 4: "Осень"}
b = int(input("Введите номер месяца "))
if b < 3 or b == 12:
    print(seasons.get(1))
elif b > 2 and b < 6:
    print(seasons.get(2))
elif b > 5 and b < 9:
    print(seasons.get(3))
elif b > 8 and b < 12:
    print (seasons.get(4))


