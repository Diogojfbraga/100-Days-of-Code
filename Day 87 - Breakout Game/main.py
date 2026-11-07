from turtle import Screen
from block import Block
from paddle import Paddle
# from ball import Ball
import random


# -------------------- Screen setup --------------------

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

paddle_position = -250

WALL_LIMIT_X_RIGHT = SCREEN_WIDTH / 2 - 10
WALL_LIMIT_X_LEFT = -SCREEN_WIDTH / 2 + 10

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Breakout Game")
screen.colormode(255)

# Enable automatic screen updates for keyboard movement
screen.tracer(1)


# -------------------- Create game objects --------------------

# Paddle
paddle = Paddle((0, paddle_position), SCREEN_WIDTH)


# -------------------- Create blocks --------------------

BLOCK_GAP = 5
BLOCK_HEIGHT = 45

blocks = []

## Create three rows of blocks
for row in range(3):

    x = WALL_LIMIT_X_LEFT
    y = 250 - (row * BLOCK_HEIGHT)

    ## Fill each row with blocks of different sizes
    while x + 20 <= WALL_LIMIT_X_RIGHT:

        # Check remaining space
        remaining_space = WALL_LIMIT_X_RIGHT - x

        # Random block width between 1 and 5
        max_width = min(5, int(remaining_space / 20))
        block_width = random.randint(1, max_width)

        # Convert width into pixels
        width_pixels = block_width * 20

        # Calculate the centre of the block
        block_x = x + width_pixels / 2

        # Generate random colours
        block_color_red = random.randint(0, 255)
        block_color_green = random.randint(0, 255)
        block_color_blue = random.randint(0, 255)

        # Create the block
        block = Block(
            (block_x, y),
            block_width,
            block_color_red,
            block_color_green,
            block_color_blue
        )

        # Store block for collision detection
        blocks.append(block)

        # Move to the next available position
        x += width_pixels + BLOCK_GAP


# -------------------- Controls --------------------

screen.listen()

# Paddle controls
screen.onkey(paddle.move_left, "a")
screen.onkey(paddle.move_right, "d")

# Also support arrow keys
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")


# -------------------- Main game loop --------------------

screen.mainloop()