# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)


bids = {}
continue_bidding = True

while continue_bidding:
    print("\n" * 100)
    name = input("What is your name?: ")
    price = int(input("What is your bid price?: "))
    bids[name] = price
    should_continue = input("There are other users who want to bid?: yes or no: ").lower()
    if should_continue == "no":
        continue_bidding = False
        find_higheste_bidder(bids)


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of $ {highest_bid}")



