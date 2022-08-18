import random

print("загадайте число от 0 до 100")
print(
    "Если число меньше или больше вашего вводите '<' или '>' соответственно, а если я угадал, то введите 'Да' и нажмите Enter"
)
rnd = 50
min_diapazona = 0
max_diapazona = 100
otvet = ""
while 1 > 0:
    print("Мое число:", rnd, "я угадал? Диапазон от", min_diapazona, "до", max_diapazona)
    otvet = input()
    if otvet == "Да":
        print("Я угадал! Игра окончена.")
        break
    elif otvet == "<":
        max_diapazona = rnd - 1
        try:
            rnd = random.randint(min_diapazona, max_diapazona)
        except:
            print("не честно, Игра окончена!")
    elif otvet == ">":
        min_diapazona = rnd + 1
        try:
            rnd = random.randint(min_diapazona, max_diapazona)
        except:
            print("не честно, Игра окончена!")
            break
    else:
        print("Ввод неправильный, Допустимые символы: '<', '>' и 'y'")
        with open('results.txt', 'a') as file:
            file.write(f'{dict(max_diapazona=max_diapazona, min_diapazona=min_diapazona, rnd=rnd)}\n')