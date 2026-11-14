from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("circle")
        self.penup()

        # Ball movement
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Move the ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Bounce against the side walls
    def bouce_wall(self):
        self.x_move *= -1

    # Bounce against the paddle or top wall
    def bouce_paddle(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    # Reset the ball
    def ball_reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move = random.choice([-10, 10])
        self.y_move = 10