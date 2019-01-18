from os import path
from random import randint, choice


if __name__ == "__main__":
    with open('tickets.txt', 'w') as f:
        f.write(choice(('Simple', 'Difficult', 'Mixed'))+'\n')
        i = ''
        while not i.isdigit():
            i = input('Введите желаемое количество билетов:')
        if i.isdigit():
            i = int(i)
            for j in range(i):
                f.write(str(randint(100000, 999999))+'\n')

