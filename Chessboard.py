"""
Program builds chessboard
"""
class Chess:
    def __init__(self, height=0, width=0):
        self.height = int(height)
        self.width = int(width)
        pass
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

print('Введите параметры шахматной доски.\nЗначиения должны быть целыми положительными')
h = ''
w = ''
while not str.isdigit(h):
    h = input('Высота = ')
    if not str.isdigit(h): print('Введите корректное значение')

while not str.isdigit(w):
    w = input('Ширина = ')
    if not str.isdigit(w): print('Введите корректное значение')

v = Chess(h,w)
print(v)
