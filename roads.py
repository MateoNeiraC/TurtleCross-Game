from turtle import Turtle


class Road(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)

    def move(self, position):
        self.goto(position)
