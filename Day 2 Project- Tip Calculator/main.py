"""
This is the Day 2 Project of 100 day of coding course from Udemy
In this Project I have applied what I have learned in Day 2 like
- Data Types
- Input
- F String
- Input
- Mathematical Logic
"""

# ---------------------------------------------------------------
## If the bill was $150.00, split between 5 people, with 12% tip.
## each person should pay (150.00/ 5) * 1.12 = 33.6$
## Format the result to 2 Decimal places = 33.60
print("Welcome to the Tip Calculator.")

#? This takes input from users and turns it into float dt. 
bill = float(input("What was the total bill? $"))

#? This takes input from uses and turns it into integer dt.
tip = int(input("How much tip would you like to give? 10, 12, 15?"))

#? This takes input from user for people and turns it into integer dt.
people = int(input("How many people to split the bill?"))

#? This converts tip integer into percentage
tip_as_percent = tip/100

#? This Calculate Total tipp amount from Bill
total_tip_amount = bill * tip_as_percent

#? This Calculate Total Bill amount by adding tip amount
total_bill = bill + total_tip_amount

#? This splits the bill between people
bill_pre_person = total_bill/people

#? This is the final amount to be paid by an individual in a group
final_amount = round(bill_pre_person, 2)

#? This prints the Final amount in terminal
print(f"Each person should pay ${final_amount}")


