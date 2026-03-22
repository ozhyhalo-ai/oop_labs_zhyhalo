from math import pi

class Triangle:
    def __init__(self, a, b, c):
        assert a+b > c and a+c > b and c+b > a, "Не трикутник"
        self.a = a
        self.b = b
        self.c = c

    def perimeter (self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2.0 #Обчислюємо півпериметр
        res = p * (p - self.a) * (p - self.b) * (p - self.c)
        return res ** 0.5

    def __str__(self):
        return f"Трикутник(a={self.a}, b={self.b}, c={self.c})"

class Rectangle:
    def __init__(self, a, b):
        assert a>0 and b>0, "Нк прямокутник"
        self.a = a
        self.b = b

    def perimeter (self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def __str__(self):
        return f"Прямокутник(a={self.a}, b={self.b})"

class Trapeze:
    def __init__(self, a, b, c, d):
        # a, b - основи; c, d - бічні сторони
        assert a>0 and b>0 and c>0 and d>0
        assert a!=b
        # знаходимо різницю основ і зберігаємо її в self
        self.x = abs(a - b)
        assert self.x + c > d and self.x + d > c and c + d > self.x

        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        p = (self.x + self.c + self.d) / 2.0
        s_tri = (p * (p - self.x) * (p - self.c) * (p - self.d)) ** 0.5
        # знаходимо висоту
        h = (2 * s_tri) / self.x
        return ((self.a + self.b) / 2.0) * h

    def __str__(self):
        return f"Трапеція(a={self.a}, b={self.b}, c={self.c}, d={self.d})"

class Parallelogram:
    def __init__(self, a, b, h):
        # a, b - сторони, h - висота
        assert a > 0 and b > 0 and h > 0
        assert h <= a or h <= b

        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h

    def __str__(self):
        return f"Паралелограм(a={self.a}, b={self.b}, h={self.h})"

class Circle:
    def __init__(self, r):
        assert r > 0

        self.r = r

    def perimeter(self): # це довжина кола! названа периметром, для зручного використання потім в обробці
        return 2*pi*self.r

    def area(self):
        return pi*self.r**2

    def __str__(self):
        return f"Круг(r={self.r})"

valid_shapes = [] # порожній список, куди складаємо всі правильні фігури

files = ['input01.txt', 'input02.txt', 'input03.txt']
for i in files:
    print(f"\nОбробка файла {i}")

    with open(i, 'r') as file:
        # читаємо рядки
        for line in file:
            # розбиваємо рядок на список слів
            word_list = line.split()
            # якщо рядок був порожній, пропускаємо його
            if len(word_list) == 0:
                continue

            shape = word_list[0] # перше слово це назва фігури

            if shape == 'Triangle':
                a = float(word_list[1])
                b = float(word_list[2])
                c = float(word_list[3])

                try:
                    t = Triangle(a, b, c)
                    valid_shapes.append(t)
                except AssertionError:
                    continue

            elif shape == 'Rectangle':
                a = float(word_list[1])
                b = float(word_list[2])

                try:
                    r = Rectangle(a, b)
                    valid_shapes.append(r)
                except AssertionError:
                    continue

            elif shape == 'Trapeze':
                a = float(word_list[1])
                b = float(word_list[2])
                c = float(word_list[3])
                d = float(word_list[4])

                try:
                    trap = Trapeze(a, b, c, d)
                    valid_shapes.append(trap)
                except AssertionError:
                    continue

            elif shape == 'Parallelogram':
                a = float(word_list[1])
                b = float(word_list[2])
                h = float(word_list[3])

                try:
                    p = Parallelogram(a, b, h)
                    valid_shapes.append(p)
                except AssertionError:
                    continue

            elif shape == 'Circle':
                r = float(word_list[1])

                try:
                    c = Circle(r)
                    valid_shapes.append(c)
                except AssertionError:
                    continue

    print(f"У список додано {len(valid_shapes)} правильних фігур")

    if len(valid_shapes) > 0:
        max_area_shape = valid_shapes[0]
        max_perimeter_shape = valid_shapes[0]

        for shape in valid_shapes:
            if shape.area() > max_area_shape.area():
                max_area_shape = shape
            if shape.perimeter() > max_perimeter_shape.perimeter():
                max_perimeter_shape = shape

        print(f"Найбільша площа: {max_area_shape} ({max_area_shape.area():.2f})")
        print(f"Найбільший периметр: {max_perimeter_shape} ({max_perimeter_shape.perimeter():.2f})")

    valid_shapes = []

'''
print(f"У список додано {len(valid_shapes)} правильних фігур")
'''

'''
for shape in valid_shapes:
    name = shape.__class__.__name__ # дістаємо назву фігури
    print(f"Фігура: {name} | Периметр: {shape.perimeter():.2f} | Площа: {shape.area():.2f}")
'''

'''
if len(valid_shapes) > 0:
    max_area_shape = valid_shapes[0]
    max_perimeter_shape = valid_shapes[0]

    for shape in valid_shapes:
        if shape.area() > max_area_shape.area():
            max_area_shape = shape
        if shape.perimeter() > max_perimeter_shape.perimeter():
            max_perimeter_shape = shape

    print(f"Найбільша площа: {max_area_shape.__class__.__name__} ({max_area_shape.area():.2f})")
    print(f"Найбільший периметр: {max_perimeter_shape.__class__.__name__} ({max_perimeter_shape.perimeter():.2f})")
'''