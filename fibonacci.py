

class Fibonacci:
    def __init__(self, last, first):
        self.first = first
        self.last = last
        self.list = self.fib(first, last)

    def validation(self):
        if (type(self.first) != int) or (type(self.last) != int):
            raise TypeError('Числа должны быть целые')
        if self.first < 0 or self.last < 0:
            raise ValueError('Числа должны быть положительные')
        return True

    def fib(self, first, last):
        self.validation()
        if last < first:
            last, first = first, last

        fib_list = []
        a = 0
        b = 1
        while a <= last:
            if first <= a <= last:
                fib_list.append(a)
            a, b = b, a + b
        return fib_list

    def __repr__(self):
        return ', '.join(map(str, self.list))

obj = Fibonacci(10,100)
print(obj)