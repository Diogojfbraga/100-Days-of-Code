from art import ascii_art

import random

# Possible Blackjack card values.
# There are four 10s because 10, Jack, Queen, and King all have a value of 10.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Ask the player if they want to start the game.
start = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': "
).lower()

game_on = True

# End the program if the player does not choose 'y'.
if start == 'y':
    game_on = True
else:
    exit()

# Give the player two random cards.
player_cards = [random.choice(cards), random.choice(cards)]

print(
    f'     Your cards: {player_cards}, '
    f'current score: {player_cards[0] + player_cards[1]}'
)

# Give the computer two random cards.
computer_cards = [random.choice(cards), random.choice(cards)]

# Only show the computer's first card.
print(f"     Computer's first card: {computer_cards[0]}")


# Keep running the game until someone wins, loses, or draws.
while game_on:

    # Check whether the player has a score of 21.
    if sum(player_cards) == 21:
        print("You have Blackjack!\nYou Win!")
        game_on = False

    # Check whether the computer has a score of 21.
    elif sum(computer_cards) == 21:
        print(computer_cards)
        print("Computer has Blackjack!\nYou Lose!")
        game_on = False

    # Check whether the player's score is over 21.
    elif sum(player_cards) > 21:

        # If the player has an Ace worth 11,
        # change it to 1 to reduce the total score.
        if 11 in player_cards:
            index = player_cards.index(11)
            player_cards[index] = 1

            # Check whether the player is still over 21.
            if sum(player_cards) > 21:
                print(
                    f"Total: {sum(player_cards)}. "
                    "You are bust. Computer won."
                )
                game_on = False

        # If there is no Ace to change, the player is bust.
        else:
            print(
                f"Total: {sum(player_cards)}. "
                "You are bust. Computer won."
            )
            game_on = False

    # Check whether the computer's score is over 21.
    elif sum(computer_cards) > 21:

        # If the computer has an Ace worth 11,
        # change it to 1.
        if 11 in computer_cards:
            index = computer_cards.index(11)
            computer_cards[index] = 1

            # Check whether the computer is still bust.
            if sum(computer_cards) > 21:
                print(
                    f"Total: {sum(computer_cards)}. "
                    "Computer is bust. You won."
                )
                game_on = False

            # If the computer is no longer bust and has a higher score,
            # the computer wins.
            elif sum(computer_cards) >= sum(player_cards):
                print(
                    f'"Computer wins" '
                    f'Player score: {sum(player_cards)} / '
                    f'Computer score: {sum(computer_cards)}'
                )
                game_on = False

        # If the computer has no Ace to change, it is bust.
        else:
            print(
                f"Total: {sum(computer_cards)}. "
                "Computer is bust. You won."
            )
            game_on = False

    # Continue while the player's score is below 21.
    elif sum(player_cards) < 21:

        # Ask whether the player wants another card.
        next_card = input(
            "Do you want another card? Type 'y' or 'n': "
        ).lower()

        # Give the player another card.
        if next_card == 'y':
            next_card = random.choice(cards)

            print(f'Your next card is: {next_card}')

            player_cards.append(next_card)

            print(f'Player total: {sum(player_cards)}')

        # If the player stops and both scores are equal, it is a draw.
        elif (
            next_card == 'n'
            and sum(computer_cards) == sum(player_cards)
        ):
            print(
                f'"Draw" Player score: {sum(player_cards)} / '
                f'Computer score: {sum(computer_cards)}'
            )
            game_on = False

        # If the player stops, the computer starts drawing cards.
        elif next_card == 'n':

            # The computer draws until its score reaches
            # or passes the player's score.
            while sum(computer_cards) < sum(player_cards):
                computer_next_card = random.choice(cards)

                print(
                    f'Computer next card is: '
                    f'{computer_next_card}'
                )

                computer_cards.append(computer_next_card)

                print(
                    f'Computer total: {sum(computer_cards)}'
                )

                # Stop drawing if the computer goes over 21.
                if sum(computer_cards) > 21:
                    break

            # Check whether the computer is bust.
            if sum(computer_cards) > 21:
                print(
                    f'"You win" '
                    f'Player score: {sum(player_cards)} / '
                    f'Computer score: {sum(computer_cards)}'
                )
                game_on = False

            # Check whether the computer has a higher score.
            elif sum(computer_cards) > sum(player_cards):
                print(
                    f'"Computer wins" '
                    f'Player score: {sum(player_cards)} / '
                    f'Computer score: {sum(computer_cards)}'
                )
                game_on = False

            # Check whether both scores are equal.
            elif sum(computer_cards) == sum(player_cards):
                print(
                    f'"Draw" '
                    f'Player score: {sum(player_cards)} / '
                    f'Computer score: {sum(computer_cards)}'
                )
                game_on = False

        # Handle invalid input.
        else:
            print("Please type 'y' or 'n'.")

    else:
        print("Continue")
        game_on = False