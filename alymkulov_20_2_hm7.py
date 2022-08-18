ten = list(range(1, 11))
evens = list(filter(lambda x: x%2 == 0, ten))
squared = list(map(lambda x: x**2, evens))

def index(list = ten):
    while True:
        try:
            ask = int(input("Ведите индекс: "))
            print(list[ask])
            continue

        except:
            print('Введите настоящий индекс! ')
            continue
index()