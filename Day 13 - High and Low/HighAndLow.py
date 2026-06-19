from db import objects
from art import ascii_art
import random

# Controls when the main game loop should stop
game_over = False

# Stores the player's current score
score = 0


# Main game loop
while game_over is not True:
    print(ascii_art)

    # Randomly choose two items from the database
    itemA = random.choice(objects)
    itemB = random.choice(objects)

    # Make sure item A has a valid name and value
    while itemA['name'] == "" or itemA['value'] == 0:
        itemA = random.choice(objects)

    # Make sure item B has a valid name and value
    while itemB['name'] == "" or itemB['value'] == 0:
        itemB = random.choice(objects)

    # Make sure A and B are not the same item and do not have the same value
    while itemA == itemB or itemB["name"] == "" or itemB["value"] == 0 or itemA["value"] == itemB["value"]:
        itemB = random.choice(objects)

    # Display the current score and both comparison options
    print(f"Your score is: {score}")
    print(f"Compare A: {itemA['name']}\n")
    print("Vs\n")
    print(f"Compare B: {itemB['name']}\n")

    # Keep asking until the user enters a valid choice
    while True:
        try:
            user_choice = input("Which is searched more online? Type 'A' or 'B': ").lower()

            # Only allow 'a' or 'b' as valid answers
            if user_choice != "a" and user_choice != "b":
                raise ValueError

            break

        except ValueError:
            print("Please choose a valid answer!")

    # Check if A has a higher search value
    if itemA['value'] > itemB['value']:

        # User guessed A correctly
        if user_choice == 'a':
            score += 1

        # User guessed incorrectly, so end the game
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

    # If A is not higher, then B must be higher
    else:

        # User guessed B correctly
        if user_choice == 'b':
            score += 1

        # User guessed incorrectly, so end the game
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True