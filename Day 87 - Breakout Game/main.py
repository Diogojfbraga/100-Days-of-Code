from turtle import Screen
from block import Block
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
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
screen.tracer(0)


# -------------------- Create game objects --------------------

# Paddle
paddle = Paddle((0, paddle_position), SCREEN_WIDTH)

# Ball
ball = Ball()

# Scoreboard
scoreboard = ScoreBoard()


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

        # Move to the next position
        x += width_pixels + BLOCK_GAP


# -------------------- Controls --------------------

screen.listen()

# Move paddle when key is pressed
screen.onkeypress(paddle.move_left, "a")
screen.onkeypress(paddle.move_right, "d")

# Stop paddle when key is released
screen.onkeyrelease(paddle.stop_left, "a")
screen.onkeyrelease(paddle.stop_right, "d")

# Arrow keys
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

screen.onkeyrelease(paddle.stop_left, "Left")
screen.onkeyrelease(paddle.stop_right, "Right")


# -------------------- Paddle movement loop --------------------

def paddle_loop():
    if game_is_on:
        paddle.update_position()
        screen.update()
        screen.ontimer(paddle_loop, 16)


# -------------------- Main game loop --------------------

game_is_on = True

BALL_RADIUS = 10
PADDLE_HALF_WIDTH = 100
PADDLE_HALF_HEIGHT = 10


def game_loop():
    global game_is_on

    if not game_is_on:
        return

    # Keep the ball's previous position
    previous_y = ball.ycor()

    # Move the ball
    ball.move()

    # -------------------- Wall collision --------------------

    # Left and right walls
    if ball.xcor() >= WALL_LIMIT_X_RIGHT or ball.xcor() <= WALL_LIMIT_X_LEFT:
        ball.bouce_wall()

    # Top wall
    if ball.ycor() >= SCREEN_HEIGHT / 2 - BALL_RADIUS:
        ball.bouce_paddle()

    # -------------------- Paddle collision --------------------

    # Calculate where the ball touches the top of the paddle
    paddle_top = paddle.ycor() + PADDLE_HALF_HEIGHT + BALL_RADIUS

    # Check if the ball is moving down onto the paddle
    if (
        previous_y >= paddle_top
        and ball.ycor() <= paddle_top
        and abs(ball.xcor() - paddle.xcor()) <= PADDLE_HALF_WIDTH + BALL_RADIUS
    ):
        ball.bouce_paddle()

    # -------------------- Block collision --------------------

    for block in blocks:

        # Each block has a different width
        block_half_width = block.block_width * 10
        block_half_height = 20

        # Check if the ball touches the block
        if (
            abs(ball.xcor() - block.xcor()) <= block_half_width + BALL_RADIUS
            and abs(ball.ycor() - block.ycor()) <= block_half_height + BALL_RADIUS
        ):

            # Work out which side the ball hit
            overlap_x = (
                block_half_width + BALL_RADIUS
                - abs(ball.xcor() - block.xcor())
            )

            overlap_y = (
                block_half_height + BALL_RADIUS
                - abs(ball.ycor() - block.ycor())
            )

            # Bounce horizontally or vertically
            if overlap_x < overlap_y:
                ball.bouce_wall()
            else:
                ball.bouce_paddle()

            # Remove the block from the screen
            block.hideturtle()

            # Remove the block from the list
            blocks.remove(block)

            # Increase the score
            scoreboard.add_score()

            break

    # -------------------- Bottom wall --------------------

    # End game if the ball goes below the screen
    if ball.ycor() < -SCREEN_HEIGHT / 2:
        print("GAME OVER")
        game_is_on = False

    # Check if all blocks have been destroyed
    if not blocks:
        print("YOU WIN!")
        game_is_on = False

    # Update the screen
    screen.update()

    # Run the next frame
    if game_is_on:
        screen.ontimer(game_loop, 20)


# -------------------- Start game --------------------

paddle_loop()
game_loop()

screen.mainloop()