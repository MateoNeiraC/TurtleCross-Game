from turtle import Turtle

FONT = ("Courier", 24, "normal")
ACTUAL_LEVEL = 1
POSITION = (-270, 270)
MORE_LEVEL = 1


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = ACTUAL_LEVEL
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(POSITION)

    def update(self):
        self.clear()
        self.write(f'Nivel = {self.level}', False, align='left', font=FONT)

    def increase_level(self, level, increase):
        self.level += 1

