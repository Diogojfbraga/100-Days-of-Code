from turtle import Turtle


class Block(Turtle):
    def __init__(self, position, block_width, block_color_red, block_color_green, block_color_blue):
        super().__init__()

        self.shape("square")

        self.block_width = block_width
        self.block_color_red = block_color_red
        self.block_color_green = block_color_green
        self.block_color_blue = block_color_blue

        ## Set the block size and colour
        self.shapesize(stretch_len=block_width, stretch_wid=2)
        self.color((block_color_red, block_color_green, block_color_blue))

        self.penup()
        self.goto(position)