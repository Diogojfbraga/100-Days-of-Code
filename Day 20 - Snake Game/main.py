from turtle import Turtle, Screen
import time
import random


# -------------------- Screen setup --------------------

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVE_DISTANCE = 20
WALL_LIMIT = 290

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # We update the screen manually for smoother movement


# -------------------- Create snake --------------------

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
squares = []

for position in starting_positions:
    square = Turtle(shape="square")
    square.penup()
    square.color("gray", "white")
    square.goto(position)
    squares.append(square)


# -------------------- Food --------------------

def create_food():
    """Create food in a random position on the same grid as the snake."""

    new_food = Turtle(shape="circle")
    new_food.penup()
    new_food.color("green")
    new_food.shapesize(stretch_len=0.5, stretch_wid=0.5)

    # Food moves in steps of 20, matching the snake's movement.
    food_x = random.randrange(-280, 281, 20)
    food_y = random.randrange(-280, 281, 20)

    new_food.goto(food_x, food_y)
    return new_food


current_food = create_food()


# -------------------- Scoreboard --------------------

scoreboard = Turtle()
scoreboard.penup()
scoreboard.color("white")
scoreboard.hideturtle()
scoreboard.goto(0, 250)

score = 0


def update_scoreboard():
    """Remove the old score and write the new one."""
    scoreboard.clear()
    scoreboard.write(
        f"Score: {score}",
        align="center",
        font=("Arial", 18, "normal")
    )


update_scoreboard()


# -------------------- Game-over message --------------------

game_over_turtle = Turtle()
game_over_turtle.penup()
game_over_turtle.color("white")
game_over_turtle.hideturtle()


def show_game_over():
    """Show the game-over text in the middle of the screen."""
    game_over_turtle.goto(0, 0)
    game_over_turtle.write(
        "Game Over",
        align="center",
        font=("Arial", 24, "bold")
    )


# -------------------- Snake movement controls --------------------

def move_right():
    squares[0].right(90)


def move_left():
    squares[0].left(90)


# Register keys once, before the game loop.
screen.listen()
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")


# -------------------- Add snake segment --------------------

def add_segment():
    """Add one square at the current end of the snake."""

    new_square = Turtle(shape="square")
    new_square.penup()
    new_square.color("gray", "white")

    # Start hidden so it does not flash in the centre of the screen.
    new_square.hideturtle()
    new_square.goto(squares[-1].position())
    new_square.showturtle()

    squares.append(new_square)


# -------------------- Main game loop --------------------

game_is_on = True

while game_is_on:

    # Move the tail: each segment goes where the one in front was.
    for square_number in range(len(squares) - 1, 0, -1):
        new_x = squares[square_number - 1].xcor()
        new_y = squares[square_number - 1].ycor()
        squares[square_number].goto(new_x, new_y)

    # Move the head forward.
    squares[0].forward(MOVE_DISTANCE)

    # Check whether the snake has eaten the food.
    if squares[0].distance(current_food) < 15:
        score += 1
        update_scoreboard()

        add_segment()

        current_food.hideturtle()
        current_food = create_food()

    # Check collision with the wall.
    if abs(squares[0].xcor()) > WALL_LIMIT or abs(squares[0].ycor()) > WALL_LIMIT:
        show_game_over()
        print("You lost - wall collision.")
        game_is_on = False

    # Check collision with any part of the tail.
    if game_is_on:
        for tail_segment in squares[1:]:
            if squares[0].distance(tail_segment) < 10:
                show_game_over()
                print("You lost - tail collision.")
                game_is_on = False
                break

    screen.update()
    time.sleep(0.1)


screen.update()
screen.exitonclick()