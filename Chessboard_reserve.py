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
    #print('Введите параметры шахматной доски.\nЗначиения должны быть целыми положительными')
    flag = 0
    while not str.isdigit(h) or not str.isdigit(w):
        if flag != 0 or len(sys.argv[1:]) == 2: print('Полученные  размеры {} х {} некорректны\
                                                        \nВведите корректные значения:'.format(h,w))
        #print('Введите корректные значения')
        h = input('Высота = ')
        w = input('Ширина = ')
        flag += 1
        """
            if not str.isdigit(h):
            print('Введённое  значение {} некорректно'.format(h))
            continue
    #while not str.isdigit(w):
        w = input('Ширина = ')
        if not str.isdigit(w): print('Введённое  значение {} некорректно'.format(w))
        """
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
