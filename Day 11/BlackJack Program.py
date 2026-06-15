from art import ascii_art

import random 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':   ").lower()

game_on = True

if start == 'y':
    game_on = True
else:
    exit()

# Player
player_cards = [random.choice(cards) , random.choice(cards)]
print(f'     You cards: {player_cards}, current score: {player_cards[0] + player_cards[1]}')

#Computer
computer_cards = [random.choice(cards), random.choice(cards)]
print(f'     Computers first card: {computer_cards[0]}')

while game_on:
    # User got BlackJack
    if sum(player_cards) == 21:
        print("You have Blackjack!\n You Win!")
        game_on = False
    # Computer got Blackjack
    elif sum(computer_cards) == 21:
        print(computer_cards)
        print("Computer has Blackjack!\n You Lose!")
        game_on = False
    # Score is over 21
    elif sum(player_cards) > 21:
        # Does user have an Ace? If Yes, change the 1 from 11
        if 11 in player_cards:
            index = player_cards.index(11)
            player_cards[index] = 1
            # is it still over 21?
            if sum(player_cards) > 21:
                print(f"Total: {sum(player_cards)}. Your are bust. Computer won")
                game_on = False
        else:
            print(f"Total: {sum(player_cards)}. Your are bust. Computer won")
            game_on = False


    elif sum(computer_cards) > 21:
        if 11 in computer_cards:
            index = computer_cards.index(11)
            computer_cards[index] = 1
            if sum(computer_cards) > 21:
                print(f"Total: {sum(computer_cards)}. Computer Got bust. You won")
                game_on = False
            elif sum(computer_cards) >= sum(player_cards):
                print(f'"Computer wins" Player score: {sum(player_cards)} / Computer Score: {sum(computer_cards)}')
                game_on = False
            
        else:
            print(f"Total: {sum(computer_cards)}. Computer is bust. You won won")
            game_on = False

    # Player
    elif sum(player_cards) < 21:
        next_card = input("Do you want another card? 'y' or 'n'").lower()
        if next_card == 'y':
            next_card = random.choice(cards)
            print(f'Your next card is: {next_card}')
            player_cards.append(next_card)
            print(f'Player total: {sum(player_cards)}')

        elif sum(computer_cards) == sum(player_cards):
            print(f'"Draw" Player score: {sum(player_cards)} / Computer Score: {sum(computer_cards)}')
            game_on = False
        else:
            while sum(computer_cards) < sum(player_cards):
                computer_next_card = random.choice(cards)
                print(f'Computer next card is: {computer_next_card}')
                computer_cards.append(computer_next_card)
                print(f'Computer total: {sum(computer_cards)}')

                if sum(computer_cards) > 21:
                    break

            if sum(computer_cards) > sum(player_cards):
                print(f'"Computer wins" Player score: {sum(player_cards)} / Computer Score: {sum(computer_cards)}')
                game_on = False



    # Computer


            
    else:
        print("Continue")
        game_on = False
    # else:
        # print("continue")





