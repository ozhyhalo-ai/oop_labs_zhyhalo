import turtle

BOARD_X = -300
BOARD_Y = 300
BOARD_SIZE = 600
STEP = BOARD_SIZE / 3


class Figure:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def draw(self, color):
        raise NotImplementedError

    def show(self):
        self.draw("black")

    def hide(self):
        self.draw("white")





class Board(Figure):
    def __init__(self, x=BOARD_X, y=BOARD_Y, size=BOARD_SIZE):
        super().__init__(x, y)
        self.size = size

    def draw(self, color):
        turtle.pencolor(color)
        turtle.pensize(3)
        turtle.speed(0)
        turtle.hideturtle()

        step = self.size / 3

        turtle.setheading(0)
        for i in range(1, 3):
            turtle.penup()
            turtle.goto(self.x, self.y - i * step)
            turtle.pendown()
            turtle.forward(self.size)

        turtle.setheading(270)
        for i in range(1, 3):
            turtle.penup()
            turtle.goto(self.x + i * step, self.y)
            turtle.pendown()
            turtle.forward(self.size)
        turtle.setheading(0)


# хрестик
class Cross(Figure):
    def __init__(self, x=0, y=0, size=150):
        super().__init__(x, y)
        self.size = size

    def draw(self, color):
        turtle.pencolor(color)
        turtle.pensize(5)
        turtle.speed(0)
        turtle.hideturtle()

        half = self.size / 2
        turtle.penup()
        turtle. goto(self.x, self.y)

        # малюємо одну діагональ
        turtle.setheading(45)
        turtle.forward(half)
        turtle.pendown()
        turtle.backward(self.size)
        turtle.penup()

        # малюємо другу діагональ
        turtle.goto(self.x, self.y)
        turtle.setheading(135)
        turtle.forward(half)
        turtle.pendown()
        turtle.backward(self.size)
        turtle.penup()

        turtle.setheading(0)


# нулик
class Nought(Figure):
    def __init__(self, x=0, y=0, size=150):
        super().__init__(x, y)
        self.size = size

    def draw(self, color):
        turtle.pencolor(color)
        turtle.pensize(5)
        turtle.speed(0)
        turtle.hideturtle()

        radius = self.size / 2
        turtle.penup()
        turtle. goto(self.x, self.y - radius)

        turtle.setheading(0)
        turtle.pendown()
        turtle.circle(radius)
        turtle.penup()





game_board = Board()

grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

current_turn = "X"
game_over = False

def get_center(row, col):
    x = BOARD_X + col * STEP + STEP / 2
    y = BOARD_Y - row * STEP - STEP / 2
    return x, y

def draw_win_line(star_pos, end_pos):
    turtle.pencolor("red")
    turtle.pensize(10)
    turtle.penup()
    turtle.goto(star_pos)
    turtle.pendown()
    turtle.goto(end_pos)
    turtle.penup()

def announce_winner(message, color="black", bg_color="pink"):
    turtle.penup()
    turtle.goto(0, 0)

    # малюємо фон (прямокутник)
    turtle.fillcolor(bg_color)
    turtle.begin_fill()

    width = 500
    height = 100
    turtle.goto(-width / 2, 0 - height / 2)
    turtle.setheading(0)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

    # пишемо текст поверх фону
    turtle.goto(0, -25)
    turtle.pencolor(color)
    turtle.write(message, align="center", font=("Times new roman", 40, "bold"))



def check_win():
    global game_over

    # перевіряємо лінії
    for row in range(3):
        if grid[row][0] == grid[row][1] == grid[row][2] and grid[row][0] is not None:
            game_over = True
            draw_win_line(get_center(row, 0), get_center(row,2))
            announce_winner(f"Перемога: {grid[row][0]}!")
            return

    # перевіряємо стовпці
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] is not None:
            game_over = True
            draw_win_line(get_center(0, col), get_center(2, col))
            announce_winner(f"Перемога: {grid[0][col]}!")
            return

    # перевіряємо діагональ \
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] is not None:
        game_over = True
        draw_win_line(get_center(0, 0), get_center(2, 2))
        announce_winner(f"Перемога: {grid[0][0]}!")
        return

    # перевіряємо діагональ /
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] is not None:
        game_over = True
        draw_win_line(get_center(0, 2), get_center(2, 0))
        announce_winner(f"Перемога: {grid[0][2]}!")
        return

def is_board_full():
    for row in grid:
        if None in row:
            return False
    return True



# функція гри (обробка кліків)
def play(x, y):
    global current_turn, game_over

    if game_over:
        return

    col = int((x - BOARD_X) // STEP)
    row = int((BOARD_Y - y) // STEP)

    if 0 <= col < 3 and 0 <= row < 3:
        # перевіряємо в пам'яті, чи ця клітинка вільна
        if grid[row][col] is None:
            # обчислюємо координати центру потрібної клітинки
            cell_center_x, cell_center_y = get_center(row, col)

            # малюємо фігуру і записуємо її в пам'ять
            if current_turn == "X":
                new_figure = Cross(cell_center_x, cell_center_y, size=150)
                grid[row][col] = "X"
                current_turn = "O"
            else:
                new_figure = Nought(cell_center_x, cell_center_y, size=150)
                grid[row][col] = "O"
                current_turn = "X"

            new_figure.show()

            check_win()

            if not game_over and is_board_full():
                game_over = True
                announce_winner("Нічия!", color="white", bg_color="gray")


game_board.show()
turtle.onscreenclick(play)
turtle.done()