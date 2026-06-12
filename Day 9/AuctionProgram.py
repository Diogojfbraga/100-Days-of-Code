from AuctionGavel import auction_gavel
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


end = False
bidders = {}

print(auction_gavel)

while end is False:

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bidders[name] = bid

    other_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no': "
    ).lower()

    if other_bidders == "no":
        highest_bid = 0
        winner = ""

        for bidder in bidders:
            current_bid = bidders[bidder]

            if current_bid > highest_bid:
                highest_bid = current_bid
                winner = bidder

        print(f"The winner is {winner} with a bid of ${highest_bid}.")
        end = True
    else:
        clear()