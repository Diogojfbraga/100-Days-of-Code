# Rock Paper Scissors ASCII Art

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# # Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

import random

print("Lets start")

game_images = [rock, paper, scissors]
game_names = ["rock", "paper", "scissors"]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors?\n"))
computer_choice = random.randint(0,2)

# Rock
if player_choice == 0: 
    print(f"You chose {game_names[player_choice]}")
    print(game_images[player_choice])
    print(computer_choice)
    if computer_choice == 1:
        print(f"Computer chose: {game_names[computer_choice]}\n{game_images[computer_choice]}")
        print("You lose")
    elif computer_choice == 0:
        print(f"Computer chose: {game_names[computer_choice]}\n{game_images[computer_choice]}")
        print("It is a draw")
    else:
        print(f"Computer chose: {game_names[computer_choice]}\n{game_images[computer_choice]}")
        print("You won")

# Paper
elif player_choice == 1: 
    print(f"You chose {game_names[player_choice]}")
    print(game_images[player_choice])
    print(computer_choice)
    if computer_choice == 0:
        print(f"Computer chose: {game_names[computer_choice]}\n{game_images[computer_choice]}")
        print("You won")
    elif computer_choice == 1:
        print(f"Computer chose: {game_names[computer_choice]}\n{game_images[computer_choice]}")
        print("It is a draw")
    else:
        print(f"Computer chose: {game_names[computer_choice]}\n{game_images[computer_choice]}")
        print("You lose")


# Scissors
elif player_choice == 2: 
    print(f"You chose {game_names[player_choice]}")
    print(game_images[player_choice])
    print(computer_choice)
    if computer_choice == 0:
        print(f"Computer chose: {game_names[computer_choice]}\n{game_images[computer_choice]}")
        print("You lose")
    elif computer_choice == 1:
        print(f"Computer chose: {game_names[computer_choice]}\n{game_images[computer_choice]}")
        print("It is a draw")
    else:
        print(f"Computer chose: {game_names[computer_choice]}\n{game_images[computer_choice]}")
        print("You win")

else:
    print("That is a invalid number")