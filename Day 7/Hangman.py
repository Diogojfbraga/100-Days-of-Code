# Imports the random module so we can randomly select a word
import random

# Imports the word list and hangman stages from separate files
from WordList import word_list
from Stages import stages

# Randomly selects one word from the word list
chosen_word = random.choice(word_list)

# Creates an empty string to hold the hidden word display
spaces = ""

# Adds one underscore for each letter in the chosen word
for space in chosen_word:
    spaces += "_"

# Prints the hidden word
print(spaces)

# Prints the chosen word for testing/debugging
print(chosen_word)

# Controls whether the game should continue running
game_over = False 

# Stores letters that have been guessed correctly
correct_letters = []

# Stores all letters that have already been guessed
guessed_letters = []

# Sets the number of lives the player starts with
lives = 6

# Keeps the game running until game_over becomes True
while not game_over:

    # Gets the player's guess and converts it to lowercase
    guess = input("Guess a letter ").lower()

    # Creates an empty string to build the current word display
    word = ""

    # Checks if the player has already guessed this letter before
    if guess in guessed_letters:
        print("You already guessed that letter")

    # Loops through each letter in the chosen word
    for letter in chosen_word:

        # If the current letter matches the player's guess
        if letter == guess:
            word += letter
            print("That is a correct letter.")

            # Adds the correct guess to the correct_letters list
            correct_letters.append(guess)

            # Adds the guess to the guessed_letters list
            guessed_letters.append(guess)

        # If the current letter was already guessed correctly before
        elif letter in correct_letters:
            word += letter

        # If the letter has not been guessed yet, show an underscore
        else:
            word += "_"

            # Adds the guess to the guessed_letters list
            guessed_letters.append(guess)

    # Prints the current state of the guessed word
    print(word)

    # Checks if there are no more underscores, meaning the player has won
    if "_" not in word:
        game_over = True
        print("You Won")

    # Checks if the guessed letter is not in the chosen word
    if guess not in chosen_word:

        # Removes one life
        lives -= 1

        # Shows the hangman stage for the current number of lives
        print(f'That letter is not in the word, you lose a life. \n {stages[lives]}')

        # Checks if the player has run out of lives
        if lives == 0:
            print("Game Over")

    # Prints the number of lives remaining
    print(f"\nGuesses left: {lives}")