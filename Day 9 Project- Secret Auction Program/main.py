"""
This is the Day 9 Project of 100 Days of coding course from Udemy.
In this Project I have applied what I have learned on Day 9
- Clear()
- Def (Functions)
- while loop
- Dictionaries
- Nested List and Dictionaries
"""

# Importing clear function from replit package
from replit import clear

# Creating empty dictionary. Here all the bidders and their bids will be added
bids = {}
bidding_finished = False

# Created Function (find_highest_bidder).
#? This function is used to find the highest bid from (bids{})
    #! This function will loop through bids{} dictionary and
    #! return the highest bidder in the dictionary
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            hihest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${hihest_bid}.")

# ================ MAIN ==============================
#? This logic is for adding more bidders
    #! If user input "no" for question "Are there any other bidders?"
    #! Then bidding_finished = True
    #! which will exit the while loop
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_countinue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_countinue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
        print(bids)
    elif should_countinue == 'yes':
        clear()