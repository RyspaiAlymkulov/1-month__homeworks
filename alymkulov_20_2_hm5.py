flags = {
    "Kyrgyzstan": {'yellow', 'red'},
    "Estonia": {'blue', 'black', 'white'},
    "Russia": {'white', 'blue', 'red'},
    "Usa": {'white', 'red', 'blue'},
    "Germany": {'black', 'red', 'yellow'},
    "Japan": {'red', 'white'},
    "Ukraine": {'blue', 'yellow'}


}

while True:
    ask = input(" Выберите цвет (Нажмите 'q' чтобы выйти): ").lower()
    if ask == 'q':
        print('Программа остановлена')
        break

    for key, value in flags.items():
        if set(ask.split()).issubset(value):
            print(key)