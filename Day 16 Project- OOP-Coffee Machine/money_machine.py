"""
This class (MoneyMachine) is created to be used in main.py
Function: This class handles all money related things in a Coffee Maker
"""

class MoneyMachine:

    #! This is Global Scope for Currency
    CURRENCY = "$"

    #! This is Global Scope for Coine Values
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    #? Initializing profit and money_received variables
    def __init__(self):
        self.profit = 0
        self.money_received = 0

    #? This function (report) is used to print the profit.
    #* This takes profit variable from __init__ function and print it.
    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    #? This function (process_coins) is used to take input from user.
    #* This function takes couins like quarter, dime etc. from the used and add it in money_received variable
    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    #? This function (make_payment) is used to compare the cost of the product and money recieved from the user.
    #* If money_received from user is greater then or equal to cost of the product This function will return True.
    #* Else it will return False
    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
