from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, screen_width):
        super().__init__()

        self.screen_width = screen_width

        self.shape("square")
        self.shapesize(stretch_len=10, stretch_wid=1)
        self.color("white")
        self.penup()
        self.goto(position)

    ## Move paddle left
    def move_left(self):
        new_x = self.xcor() - 20

        if new_x >= -(self.screen_width / 2 - 100):
            self.goto(new_x, self.ycor())

    ## Move paddle right
    def move_right(self):
        new_x = self.xcor() + 20

        if new_x <= self.screen_width / 2 - 100:
            self.goto(new_x, self.ycor())