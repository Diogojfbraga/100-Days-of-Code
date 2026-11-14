from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, screen_width):
        super().__init__()

        self.screen_width = screen_width
        self.move_speed = 12
        self.direction = 0

        self.shape("square")
        self.shapesize(stretch_len=10, stretch_wid=1)
        self.color("white")
        self.penup()
        self.goto(position)

    ## Move paddle left
    def move_left(self):
        self.direction = -1

    ## Move paddle right
    def move_right(self):
        self.direction = 1

    ## Stop moving
    def stop_left(self):
        if self.direction == -1:
            self.direction = 0

    def stop_right(self):
        if self.direction == 1:
            self.direction = 0

    ## Update paddle position
    def update_position(self):
        new_x = self.xcor() + (self.move_speed * self.direction)

        # Keep paddle inside the screen
        left_limit = -(self.screen_width / 2 - 100)
        right_limit = self.screen_width / 2 - 100

        new_x = max(left_limit, min(new_x, right_limit))

        self.setx(new_x)