class Numbers:
    def __init__(self, number):
        self.number = self.validation(number)
        self.list = self.sequence(number)

    def validation(self, number):
        if type(number) != int and type(number) != float:
            raise TypeError('Введено не число')
        return abs(round(number))

    def sequence(self, number):
        n = self.validation(number)
        return [i for i in range(round(n ** 0.5) + 1) if i <= number]

    def __repr__(self):
        return ', '.join(map(str, self.list))

obj = Numbers(17)
print(obj)