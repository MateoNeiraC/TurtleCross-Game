from turtle import Turtle

STARTING_POSITION = (0, -260)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('white')
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)

    def move_player(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def level_complete(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def new_level(self):
        self.goto(STARTING_POSITION)
