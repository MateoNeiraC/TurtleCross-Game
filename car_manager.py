from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self,):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self, position):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new = Turtle()
            new.penup()
            new.shape('square')
            new.color(random.choice(COLORS))
            new.setheading(180)
            new.shapesize(stretch_wid=1, stretch_len=2)
            new.goto(position)
            self.all_cars.append(new)

    def movement(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def choque(self, player):
        for car in self.all_cars:
            if car.distance(player) <= 20:
                return True

    def new_level(self):
        self.speed += MOVE_INCREMENT


