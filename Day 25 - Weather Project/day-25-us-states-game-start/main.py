import turtle
from pathlib import Path

import pandas as pd


# -------------------- Screen setup -------------------- #

screen = turtle.Screen()
screen.title("U.S. States Game")

# Get the image file from the same folder as this Python file
image = Path(__file__).parent / "blank_states_img.gif"

# Add the map image as a turtle shape and display it
screen.addshape(str(image))
turtle.shape(str(image))


# -------------------- Load state data -------------------- #

# Get the CSV file from the same folder as this Python file
data_path = Path(__file__).parent / "50_states.csv"

# Read the state names and coordinates
data = pd.read_csv(data_path)

# Convert the state column into a normal Python list
all_states = data.state.to_list()

# This will store all correct guesses
guessed_states = []


# -------------------- Game loop -------------------- #

while len(guessed_states) < 50:
    # Ask the user for a state name
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What is another state's name?"
    ).title()

    # If the user types Exit, save the missing states and stop the game
    if answer_state == "Exit":
        states_to_learn = []

        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)

        # Save missing states into a new CSV file
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")

        break

    # If the guess is correct, write the state name on the map
    if answer_state in all_states:
        guessed_states.append(answer_state)

        # Create a turtle to write the state name
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()

        # Get the row for the guessed state
        state_data = data[data.state == answer_state]

        # Move to the correct coordinates and write the state name
        writer.goto(state_data.x.item(), state_data.y.item())
        writer.write(state_data.state.item())


# Keep the screen open until clicked
screen.exitonclick()