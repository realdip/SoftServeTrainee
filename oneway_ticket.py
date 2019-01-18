
from os import path


def lucky_check(lst, key):
    key = key.lower()
    if key == 'moscow':
        if sum(lst[:3]) == sum(lst[3:]):
            return 1
        return 0
    if key == 'peter':
        if sum(lst[::2]) == sum(lst[::-2]):
            return 1
        return 0
    if key == 'dnipro':
        countable = sum([i for i in lst if i % 2 == 0])
        uncountable = sum([i for i in lst if i % 2 == 1])
        if countable == uncountable:
            return 1
        return 0


def lucky_counter(key, start=1, end=999_999):
    count = 0
    blank = [0, 0, 0, 0, 0, 0]
    for number in range(start, end + 1):
        new = [int(i) for i in str(number)]
        lst = blank[:(6 - len(new))] + new
        count += lucky_check(lst, key)
    return count


def terminal():
    heare = path.abspath('.')
    repeat = True

    while repeat:
        f = input('FILE PASS: ')
        file_path = path.join(heare, f)
        print(file_path)

        if path.isfile((file_path)):
            with open(file_path) as f:
                text = f.read().lower()
                print('Text from file:', text)
                for key in ('dnipro', 'moscow', 'peter'):
                    if key in text:
                        print(key, (lucky_counter(key)))
        else:
            print('FILE NOT FOUND')

        question = input("[Y/N] to continue: ").lower()
        if question not in ('yes', 'y'):  # or just press ENTER
            repeat = None


if __name__ == "__main__":
    terminal()
