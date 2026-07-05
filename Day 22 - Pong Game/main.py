from turtle import Turtle, Screen
from paddle import Paddle
import time
import random

# -------------------- Screen setup --------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

player_1_paddle_position = 350

WALL_LIMIT_X = SCREEN_WIDTH / 2 
WALL_LIMIT_Y = SCREEN_HEIGHT / 2 

# Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))

l_paddle = Paddle((-350, 0 ))



# Divider
# divider_line = Turtle()
# divider_line.goto(0, 300)
# divider_line.color("white")
# divider_line.setheading(270)
# divider_line.pensize(5)

# for dash in range(0, 300):
#     divider_line.pendown()
#     divider_line.forward(15)
#     divider_line.penup()
#     divider_line.forward(15)
    

# Creae and move a paddle






screen.listen()
screen.onkey(Paddle.move_up, "Up")
screen.onkey(Paddle.move_down, "Down")


game_is_on = True

while game_is_on:
    screen.update()



# Create another paddle


# Create the ball and make it move


# Dtect collision with wall and bouce


# Detect collision with paddle


# Detect when paddle misses


# Keep score 





screen.exitonclick()