from math import pi

class Figure:
    def dimention(self):
        raise NotImplementedError
    def perimetr(self):
        raise NotImplementedError
    def square(self):
        raise NotImplementedError
    def squareSurface(self):
        raise NotImplementedError
    def squareBase(self):
        raise NotImplementedError
    def height(self):
        raise NotImplementedError
    def volume(self):
        raise NotImplementedError
    




class Triangle(Figure):
    def __init__(self, a, b, c):
        assert a+b > c and a+c > b and c+b > a, "Не трикутник"
        self.a = a
        self.b = b
        self.c = c

    def dimention(self):
        return 2

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5

    def volume(self):
        return self.square()


class Rectangle(Figure):
    def __init__(self, a, b):
        assert a > 0 and b > 0, "Не прямокутник"
        self.a = a
        self.b = b

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def volume(self):
        return self.square()


class Trapeze(Figure):
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

    def dimention(self):
        return 2

    def perimetr(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        p = (self.x + self.c + self.d) / 2.0
        s_tri = (p * (p - self.x) * (p - self.c) * (p - self.d)) ** 0.5
        # знаходимо висоту
        h = (2 * s_tri) / self.x
        return ((self.a + self.b) / 2.0) * h

    def volume(self):
        return self.square()


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        # a, b - сторони, h - висота
        assert a > 0 and b > 0 and h > 0
        assert h <= a or h <= b

        self.a = a
        self.b = b
        self.h = h

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

    def volume(self):
        return self.square()


class Circle(Figure):
    def __init__(self, r):
        assert r > 0

        self.r = r

    def dimention(self):
        return 2

    def perimetr(self): # це довжина кола! названа периметром, для зручного використання потім в обробці
        return 2*pi*self.r

    def square(self):
        return pi*self.r**2

    def volume(self):
        return self.square()


class Ball(Figure):
    def __init__(self, r):
        assert r>0, "Не куля"
        self.r = r

    def dimention(self):
        return 3

    def perimetr(self):
        raise Exception

    def square(self):
        raise Exception

    def squareSurface(self):
        return 4 * pi * (self.r ** 2)

    def squareBase(self):
        raise Exception

    def height(self):
        return 2 * self.r

    def volume(self):
        return (4/3) * pi * (self.r ** 3)




class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        # super() звертається до батьківського класу (Triangle)
        # Ми передаємо йому три однакові сторони: a, a, a, щоб він побудував нам основу
        super().__init__(a, a, a)
        self._h = h

    def dimention(self):
        return 3

    def perimetr(self):
        raise Exception

    def square(self):
        raise Exception

    def height(self):
        return self._h

    def squareSurface(self):
        r_in = (self.a * 3 ** 0.5) / 6
        # Знаходимо апофему (висоту бічної грані) за теоремою Піфагора
        slant_h = (self._h ** 2 + r_in ** 2) ** 0.5
        # 3 однакові бічні грані (трикутники)
        return 3 * (0.5 * self.a * slant_h)

    def squareBase(self):
        return super().square()

    def volume(self):
        return (1/3) * self.squareBase() * self.height()


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        assert a > 0 and b > 0 and h > 0, "Не чотирикутна піраміда"
        super().__init__(a, b)
        self._h = h

    def dimention(self):
        return 3

    def perimetr(self):
        raise Exception

    def square(self):
        raise Exception

    def height(self):
        return self._h

    def squareSurface(self):
        h_a = (self._h ** 2 + (self.b / 2) ** 2) ** 0.5
        h_b = (self._h ** 2 + (self.a / 2) ** 2) ** 0.5
        # Площа двох пар протилежних трикутників
        return self.a * h_a + self.b * h_b

    def squareBase(self):
        return super().square()

    def volume(self):
        return (1/3) * self.squareBase() * self.height()


class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        assert a > 0 and b > 0 and c > 0, "Не паралелепіпед"
        super().__init__(a, b)
        self.c = c

    def dimention(self):
        return 3

    def perimetr(self):
        raise Exception

    def square(self):
        raise Exception

    def height(self):
        return self.c

    def squareSurface(self):
        return 2 * (self.a * self.c + self.b * self.c)

    def squareBase(self):
        return super().square()

    def volume(self):
        return self.a * self.b * self.c


class Cone(Circle):
    def __init__(self, r, h):
        assert r > 0 and h > 0, "Не конус"
        super().__init__(r)
        self._h = h

    def dimention(self):
        return 3

    def perimetr(self):
        raise Exception

    def square(self):
        raise Exception

    def height(self):
        return self._h

    def squareSurface(self):
        # Твірна конуса (гіпотенуза з радіуса та висоти)
        l = (self.r ** 2 + self._h ** 2) ** 0.5
        return pi * self.r * l

    def squareBase(self):
        return super().square()

    def volume(self):
        return (1/3) * self.squareBase() * self.height()


class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        assert a > 0 and b > 0 and c > 0 and h > 0, "Не призма"
        assert a+b > c and a+c > b and c+b > a, "Основа не є трикутником"
        super().__init__(a, b, c)
        self._h = h

    def dimention(self):
        return 3

    def perimetr(self):
        raise Exception

    def square(self):
        raise Exception

    def height(self):
        return self._h

    def squareSurface(self):
        return (self.a + self.b + self.c) * self._h

    def squareBase(self):
        return super().square()

    def volume(self):
        return self.squareBase() * self.height()





FIGURE_CLASSES = {
    'Triangle': Triangle,
    'TriangularPyramid': TriangularPyramid,
    'Rectangle': Rectangle,
    'Trapeze': Trapeze,
    'Parallelogram': Parallelogram,
    'Circle': Circle,
    'Ball': Ball,
    'QuadrangularPyramid': QuadrangularPyramid,
    'RectangularParallelepiped': RectangularParallelepiped,
    'Cone': Cone,
    'TriangularPrism': TriangularPrism
}



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

            shape_name = word_list[0] # перше слово це назва фігури

            if shape_name in FIGURE_CLASSES:
                try:
                    params = [float(x) for x in word_list[1:]]

                    # Отримуємо потрібний клас зі словника
                    figure_class = FIGURE_CLASSES[shape_name]
                    obj = figure_class(*params)
                    valid_shapes.append(obj)

                except (AssertionError, ValueError, IndexError) as e:
                    continue

    print(f"У список додано {len(valid_shapes)} правильних фігур")

    # Шукаємо найбільшу фігуру
    if len(valid_shapes) > 0:
        max_shape = valid_shapes[0]
        max_measure = max_shape.volume()

        for shape in valid_shapes:
            current_measure = shape.volume()

            if current_measure > max_measure:
                max_measure = current_measure
                max_shape = shape

        shape_name = type(max_shape).__name__

        print(f"Міра цієї фігури найбільша у цьому файлі: {shape_name}")
        print(f"Її міра: {max_measure:.2f}")
    else:
        print("У файлі не було знайдено жодної правильної фігури для порівняння.")

    valid_shapes = []