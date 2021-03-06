"""
Program builds chessboard
"""

import sys

from instructions import TEXT


class Chess:
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    def __repr__(self):
        """
        representation
        :return: string
        """
        board = []
        for i in range(self.height):
            if i % 2 == 0:
                s = ' 0 *' * (self.width//2) + ' 0' * (self.width%2)
            else:
                s = ' * 0' * (self.width//2)+ ' *' * (self.width%2)
            board.append(s)
        board = '\n'.join(board)
        return board


def chess_input_validator(h='', w=''):
    while not str.isdigit(h) or not str.isdigit(w):
        if len(sys.argv[1:]) == 2 and h != '' and w != '':
            print('Полученные  размеры {} х {} некорректны\
                  \nВведите корректные значения:'.format(h, w))
        h = input('Высота = ')
        w = input('Ширина = ')
    return int(h), int(w)


if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        print(TEXT['chesstext'])
        h, w = chess_input_validator()
        obj = Chess(h, w)
        print(obj)
    elif len(sys.argv[1:]) == 2:
        h, w = sys.argv[1:]
        h, w = chess_input_validator(h,w)
        obj = Chess(h, w)
        print(obj)
    else:
        print('Количество параметров должно быть 2 или повторите вызов без параметров')
