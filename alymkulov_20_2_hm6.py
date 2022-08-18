def rate_f(movies):
    if len(dictionary[movies]) == 0:
        return True


def film_in_dictionary(movies):
    if movies in dictionary:
        return True
    else:
        return False


def average(movies):
    mean = 0
    for key2 in dictionary[movies].keys():
        mean += dictionary[movies][key2]
    print(f'{movies} средняя оценка: {mean / len(dictionary[movies])}')


dictionary = {}

while True:
    command = input(
        f'1 - добавление \n'
        f'2 - добавить рейтинг к фильму \n'
        f'3 - просмотр рейтингов \n'
        f'4 - выход \n')
    if command == '4':
        print('Программа остановлена')
        break

    if command == '3':
        for key in dictionary.keys():
            average = 0
            if len(dictionary[key]) == 0:
                print(f'Фильм {key} не оценивался')
            else:
                for key1 in dictionary[key].keys():
                    average += dictionary[key][key1]
                print(f'Фильм {key}\n Средняя оценка: {average / len(dictionary[key])}\n')
    if command == '':
        for key in dictionary.keys():
            if rate_f(key):
                print(f'{key} не оценивался')
            else:
                average(key)
        continue

    film = input('Введите название фильма: ').capitalize()

    if command == '1':
        if film_in_dictionary(film):
            print('Фильм уже существует в списке')
        else:
            dictionary[film] = {}
            print('\n Фильм добавлен в список \n')
        continue

    elif command == '2':
        name = input('Имя пользователя: ').capitalize()
        rate = float(input('Оценка: '))
        if 0 < rate <= 10:
            dictionary[film][name] = rate
            print(f'{name} оценил(а) {film} на: {rate}\n')
        else:
            print('Рейтинг должен быть от 1 до 10')
