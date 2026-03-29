import turtle

class Stem:
    def __init__(self, top_x, top_y, bottom_x):
        self.color = "green"
        self.top_x = top_x
        self.top_y = top_y
        self.bottom_x = bottom_x

        self.bottom_y = -150 # фіксований низ екрану
        self.tie_x = 0 # точка зв'язування букета по X (центр)
        self.tie_y = -50 # точка зв'язування по Y (трохи нижче центру)

    def draw(self, t):
        # налаштовуємо пензель
        t.color(self.color)
        t.pensize(5)

        # телепортуємось у самий низ стебла (без малювання)
        t.penup()
        t.goto(self.bottom_x, self.bottom_y)
        t.pendown()

        # малюємо лінію до місця зв'язування
        t.goto(self.tie_x, self.tie_y)

        # малюємо лінію від вузла до майбутнього бутона
        t.goto(self.top_x, self.top_y)


class Petal:
    def __init__(self, petal_color):
        self.color = petal_color

    def draw(self, t, angle):
        t.setheading(angle) # повертаємося у загальному напрямку росту пелюстки
        t.color(self.color)
        t.fillcolor(self.color)

        t.begin_fill()

        # права сторона "трикутника"
        t.right(30)
        t.forward(50)

        # півколо замість третьої сторони
        t.left(30) # вирівнюємо черепашку, щоб півколо дивилося назовні
        t.circle(25, 180) # малюємо дугу з радіусом 25 на 180 градусів (півколо)

        # ліва сторона "трикутника"
        t.left(30) #повертаємося носом до центру квітки
        t.forward(50)

        t.end_fill()


class Leaf:
    def __init__(self):
        self.color = "lightgreen"

    def draw(self, t, start_x, start_y, angle):
        # переходимо на координати кріплення листка (середина стебла)
        t.penup()
        t.goto(start_x, start_y)
        t.setheading(angle)  # Повертаємо вісь листка в потрібний бік

        # шукаємо координати точок

        # йдемо по центральній осі вперед до найширшої частини листка
        t.forward(40)  # це висота нижнього "малого" трикутника

        # повертаємо на 90 градусів ліворуч і йдемо до лівого кута
        t.left(90)
        t.forward(25)  # це половина ширини листка
        left_point = t.pos()  # запам'ятовуємо координату X, Y

        # йдемо в протилежний бік до правого кута
        t.backward(50)  # 25 вліво + 25 вправо = 50 загальна ширина
        right_point = t.pos()

        # повертаємося на центральну вісь
        t.forward(50)
        t.right(90)

        # йдемо до кінчика листка (висота довгого трикутника)
        t.forward(200)
        tip_point = t.pos()

        # малюємо дельтоїд
        t.goto(start_x, start_y)
        t.color("green", self.color)
        t.pendown()
        t.begin_fill()
        t.goto(right_point)  # Малюємо лінію до правого кута
        t.goto(tip_point)  # Малюємо довгу лінію до кінчика
        t.goto(left_point)  # Малюємо довгу лінію до лівого кута
        t.goto(start_x, start_y)  # Замикаємо фігуру біля стебла
        t.end_fill()


class Flower:
    def __init__(self, top_x, top_y, bottom_x, petal_color):
        # тут відбувається композиція. Квітка створює всередині себе об'єкти інших класів
        self.top_x = top_x
        self.top_y = top_y

        self.stem = Stem(top_x, top_y, bottom_x)

        if self.top_y > 150:
            self.leaf = Leaf()
        else:
            self.leaf = None # листка нема

        self.petals = [Petal(petal_color) for _ in range(5)]

    def draw_flower(self, t):
        # викликаємо методи малювання деталей
        self.stem.draw(t)

        # якщо листок існує -> малюємо його
        if self.leaf is not None:
            # шукаємо середину між вузлом букета та бутоном (на 140 градусів)
            mid_x = (self.stem.tie_x + self.top_x) / 3
            mid_y = (self.stem.tie_y + self.top_y) / 3

            # якщо квітка зліва (top_x < 0), хилимо листок вліво (
            # якщо справа - хилимо вправо (на 40 градусів)
            leaf_angle = 150 if self.top_x < 0 else 30

            self.leaf.draw(t, mid_x, mid_y, leaf_angle)

            t.penup()
            t.goto(self.top_x, self.top_y)
            t.pendown()

        # малюємо пелюстки по колу
        current_angle = 0
        step_angle = 360 / len(self.petals) # розраховуємо кут між пелюстками

        for petal in self.petals:
            petal.draw(t, current_angle)
            current_angle += step_angle

        # малюємо жовту серединку
        t.setheading(0)
        t.color("gold")
        t.dot(30)  # ставить рівне зафарбований круг

class Bouquet:
    def __init__(self):
        # створюэмо спысок з ризных об'єктів-квітів.
        # кожна квітка - окремий, незалежний екземпляр класу Flower
        self.flowers = [
            Flower(top_x=-50, top_y=200, bottom_x=25, petal_color="purple"),
            Flower(top_x=50, top_y=200, bottom_x=-25, petal_color="red"),
            Flower(top_x=-100, top_y=100, bottom_x=50, petal_color="red"),
            Flower(top_x=100, top_y=100, bottom_x=-50, petal_color = "purple"),
            Flower(top_x=0, top_y=130, bottom_x=0, petal_color="magenta"),
        ]

    def draw_bouquet(self, t):
        # букет не містить логіки малювання ліній
        # він просто віддає це завдання кожній окремій квітці
        for flower in self.flowers:
            flower.draw_flower(t)


# Налаштовуємо полотно і створюємо черепашку
window = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(3)

# Створюємо об'єкт букета
bouquet = Bouquet()
# Передаємо черепашку букету, щоб він почав процес малювання
bouquet.draw_bouquet(my_turtle)
my_turtle.hideturtle()
turtle.done()