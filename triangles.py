

class Triangle:
    def __init__(self, name, sides, area):
        self.name = name
        self.sides = sides
        self.area = area

    def __str__(self):
        return "[{}]: {} cm²".format(self.name, self.area)

    def triangle_area(sides):
        a, b, c = sides
        p = (a + b + c) / 2
        if p <= a or p <= b or p <= c:
            return None
        area = ((p - a) * (p - b) * (p - c)) ** 0.5
        return round(area, 2)

    def create():
        name = input("Имя: ")
        valid_sides = None
        while not valid_sides:
            sides = input("Стороны через запятую: ").replace(' ', '').split(',')
            try:
                a, b, c = sides
                sides = (abs(float(a)), abs(float(b)), abs(float(c)))
            except ValueError:
                print('Некорректный ввод:', sides)
            except TypeError:
                print('Некорректный ввод:', sides)
            if len(sides) == 3:
                area = Triangle.triangle_area(sides)
                if area:
                    valid_sides = True
                    return Triangle(name, sides, area)
                else:
                    print('Ошибка ввода:', sides)
                    print('Нельзя построить треугольник по заданым сторонам')
            else:
                print("Введенное количество сторон не 3")


def start():
    new_triangles = []
    repeat = True
    while repeat:
        new_triangles.append(Triangle.create())
        answer = input("Введите 'y' или 'yes' чтобы продолжить: ").lower()
        if answer not in ('yes', 'y'):  # or just press ENTER
            repeat = None

    print('\nОтсортировано:')
    i = 1
    for self in sorted(new_triangles, key=lambda x: x.area):
        print('{}. [Треугольник {}]: {} сm²'.format(i, self.name, self.area))
        i += 1


if __name__ == "__main__":
    start()
