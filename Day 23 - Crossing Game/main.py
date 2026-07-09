import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

new_car = CarManager()
turtle = Player()
scoreboard = Scoreboard()

# -------------------- Controls --------------------
screen.listen()
screen.onkey(turtle.turtle_move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    new_car.generate_cars()
    new_car.car_move()

    for car in new_car.all_cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            screen.update()
            break

    if turtle.ycor() > 260:
        turtle.reset_turtle()
        scoreboard.level()
        new_car.increase_speed()

screen.update()
screen.exitonclick()