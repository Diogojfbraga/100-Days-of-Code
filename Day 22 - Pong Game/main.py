from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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


# -------------------- Create game objects --------------------

# Right paddle
r_paddle = Paddle((350, 0))

# Left paddle
l_paddle = Paddle((-350, 0))

# Ball
ball = Ball()

# Score
score = 0
scoreboard = Scoreboard()

# r_scoreboard = Scoreboard(score)


# -------------------- Divider --------------------

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


# -------------------- Controls --------------------

screen.listen()

# Player Left controls
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

# Player Right controls
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")


# -------------------- Main game loop --------------------

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    # Move the ball
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bouce_paddle()

    # Detect when the ball goes out of bounds

    # Left receives a point
    if ball.xcor() > 360:
        ball.ball_reset()
        scoreboard.l_point()

    # Right receives a point
    if ball.xcor() < -360:
        ball.ball_reset()
        scoreboard.r_point()




screen.exitonclick()