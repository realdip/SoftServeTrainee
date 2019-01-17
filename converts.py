OUTPUT_TEXT = (
    'Высота первого конверта: ',
    'Ширина первого конверта: ',
    'Высота второго конверта: ',
    'Ширина второго конверта: '
    )

class Letter:
    def __init__(self, h=0, w=0, h2=0, w2=0):
        self.h = h
        self.w = w
        self.h2 = h2
        self.w2 = w2

    def check(self, h, w, h2, w2):
        if max(h, w) < max(h2, w2) and min(h, w) < min(h2, w2):
            return "Первый конверт с размером {}х{} можно вложить в конверт {}х{}".format(h, w, h2, w2)
        elif max(h, w) > max(h2, w2) and min(h, w) > min(h2, w2):
            return "Второй конверт с размером {}х{} можно вложить в конверт {}х{}".format(h2, w2, h, w)
        else:
            return "Ни один из конвертов нельзя вложить в другой"


    def text_to_float(self, text):
        try:
            text = text.replace(',', '.').replace(' ', '')
            number = float(text)
        except ValueError:
            print('{} Не число, введите корректное значение'.format(text))
            return text
        return number


    def start(self):
        measures = []

        while len(measures) < 4:
            text = input(OUTPUT_TEXT[len(measures)])
            text = self.text_to_float(text)
            if type(text) == float:
                measures.append(text)

        self.h, self.w, self.h2, self.w2 = measures
        print(self.check(self.h, self.w, self.h2, self.w2))

        n = input("Хотите продолжить? Введите 'y' или 'yes' :\n").lower()
        if n in ('yes', 'y'):
            self.start()

if __name__ == "__main__":
    obj = Letter()
    obj.start()
