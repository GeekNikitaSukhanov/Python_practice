print("Первое задание")
a = 1
b = 2
c = 3
print (a,b,c)
command = input("Как часто ты пьешь пиво? ")
print(command)
drinks = int(input("Сколько кружек в день? "))
print("Пить", command, "и", drinks, "кружек пива - это ненормально")
print(" ")
print("Второе задание")
time = int(input("Введите любое количество секунд "))
print("Введенное кол-во секунд - это")
hours = time // 60 // 60
minutes = -1 * (hours * 60 - (time // 60))
seconds = time - (hours * 60 * 60) - (minutes * 60)
if hours >= 10 and minutes >= 10 and seconds >= 10:
    print(hours,"часов ", minutes, "минут ", seconds, "секунд")
else:
    if hours >=10 and minutes >= 10:
        print(hours, "часов", minutes, "минут", "0",seconds,"секунд")
    else:
        if hours>= 10:
            print(hours, "часов ","0",minutes, "минут ","0",seconds,"секунд")
        else:
            print("0",hours,"часов ","0",minutes,"минут","0",seconds,"секунд")
print(" ")
print("Третье задание")
var = int(input("Введите любое однозначное число "))
var_1 = var * 11
var_2 = var * 111
print(var + var_1 + var_2)
print(" ")
print("Четвертое задание")
a = int(input("Введите любое положительное число"))
b = a % 10
while a >=10:
    a = a // 10
    if a % 10 > b:
        b = a % 10
print("Самая большая цифра в числе", b)

print("Пятое задание")
revenue = int(input("Введите прибыль за прошлый год "))
costs = int(input("Введите расходы за прошлый год "))
a = revenue - costs
if a>0:
    print("Прибыль составила ",a)
    b = a // revenue * 100
    print("Операционная маржа бизнеса ", b, "%")
else:
    if a == 0:
        print("Предприятие вышло в ноль")
    else:
        print("Убыток составил",a)
print(" ")
print("Спортстмен каждый день занимается пробежками")
run = int(input("Введите, сколько км он пробегает сегодня"))
print("Каждый день спортсмен пробегает на 10% больше")
goal = int(input("Введите цель по длине пробежки спортстмена в день"))
day = 0
while run < goal:
    run = run * 1.1
    day = day + 1
print("Спортсмен достиг свою цель на день ", day)






