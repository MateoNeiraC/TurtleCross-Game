import time
from turtle import Screen, Turtle
from player import Player, STARTING_POSITION, FINISH_LINE_Y
from car_manager import CarManager, STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from scoreboard import Scoreboard, ACTUAL_LEVEL, MORE_LEVEL
from roads import Road
import random

screen = Screen()
screen.title('cross the road')
screen.setup(width=600, height=600)
screen.bgcolor('grey')
screen.tracer(0)


#crear las calles


positions = [
    (250, 200), (150, 200), (50, 200), (-50, 200), (-150, 200), (-250, 200),
    (250, 100), (150, 100), (50, 100), (-50, 100), (-150, 100), (-250, 100),
    (250, 0), (150, 0), (50, 0), (-50, 0), (-150, 0), (-250, 0),
    (250, -100), (150, -100), (50, -100), (-50, -100), (-150, -100), (-250, -100),
    (250, -200), (150, -200), (50, -200), (-50, -200), (-150, -200), (-250, -200),
]

for position in positions:
    road = Road()
    road.move(position)


#crear el jugador y su movimiento

score = Scoreboard()

player = Player()

screen.listen()
screen.onkey(player.move_player, 'Up')


#cars moving
car = CarManager()

car_positions = [
    (320, 250), (320, 150), (320, 50), (320, -50), (320, -150)
]


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    score.update()
    car.create_car(random.choice(car_positions))
    car.movement()
    if car.choque(player):
        game_is_on = False
    if player.level_complete():
        player.new_level()
        car.new_level()
        score.increase_level(ACTUAL_LEVEL, MORE_LEVEL)

game_over = Turtle()
game_over.penup()
game_over.hideturtle()
game_over.color('red')
game_over.write('GAME OVER', False, align='center', font=('Anton', 50, 'normal'))
screen.update()

screen.exitonclick()
