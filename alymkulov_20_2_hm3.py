while True:
    alphabet = input("\n Введите желаемое слово: (Для выхода нажмите 'q') \n").lower()
    if alphabet == 'q':
        print('Остановка программы ')
        break
    for i in alphabet:
        rus_alphabet = ('йцукенгшщзхъфывапролджэячсмитьбю!?=+')
        eng_alphabet = ("qwertyuiop[]asdfghjkl;'zxcvbnm,.!?=+")
        if i in rus_alphabet:
            print(eng_alphabet[rus_alphabet.index(i)], end='')
        else:
            print(rus_alphabet[eng_alphabet.index(i)], end='')
