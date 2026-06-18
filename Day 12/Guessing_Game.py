import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

dificulty = input(
        "Welcome to the Number Guessing Game!\n" \
        "I'm thinking of a number between 1 and 100.\n" \
        "Choose a difficulty.Type 'easy' or 'hard': ").lower()

random_number = random.randint(1,100)


def easy():
    attempts = EASY_ATTEMPTS
    while attempts > 0 :
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if random_number < guess:
            print("Too High")
            attempts -= 1
        elif random_number > guess:
            print("Too Low")
            attempts -= 1 
        else:
            print("You Guessed")
            break
    if attempts == 0:
        print(f"You lost. The number was {random_number}")


def hard():
    attempts = HARD_ATTEMPTS
    while attempts > 0 and end_game == False:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if random_number < guess:
            print("Too High")
            attempts -= 1
        elif random_number > guess:
            print("Too Low")
            attempts -= 1 
        else:
            print("You Guessed")
            end_game = True
            break
    if attempts == 0:
        print(f"You lost. The number was {random_number}")
    

if dificulty == 'easy':
    easy()
elif dificulty == 'hard':
    hard()
else:
    print("Please select a valid option!")
