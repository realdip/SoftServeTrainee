

class Fibonacci:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.list = []

    def validation(self):
        if (type(self.start) != int) or (type(self.end) != int):
            raise TypeError('Числа должны быть целые')
        if self.start < 0 or self.end < 0:
            raise ValueError('Числа должны быть положительные')
        return True

    def count(self):
        self.validation()
        if self.end < self.start:
            self.end, self.start = self.start, self.end
        a = 0
        b = 1
        while a <= self.end:
            if self.start <= a <= self.end:
                self.list.append(a)
            a, b = b, a + b

    def __repr__(self):
        return ', '.join(map(str, self.list))

obj = Fibonacci(10,100)
obj.count()
print(obj)