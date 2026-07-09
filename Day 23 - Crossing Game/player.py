STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(0,-300)

    def turtle_move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)
        
    def reset_turtle(self):
        self.goto(0,-300)