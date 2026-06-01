"""
This is the Day 15 Project of 100 Days of Coding Course from Udemy.
In this Project I have applied what I have learned until now from Day 1 to Day 15.
"""

# RECEPIES AND COST
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# RESOURCES
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 1: Checking resource sufficient by making function
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    #* Looping through MENU ingredients and comparing it with resources we have.
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


# TODO 2: Processing coins by making function
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coin.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dime?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# TODO 3: Checking transaction successful
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient,"""
    #* Comparing User money (money_received) with drink cost from MENU dictionary.
    #! If money_received is greater then or equal to drink_cost.
    if money_received >= drink_cost:
        #! If there remainning amount. Return it to user.
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        #* Adding drink cost into profit
        global profit
        profit += drink_cost
        return True
    #! Else print sorry
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO 4: Making Coffee function
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    #* Looping through MENU dictionary and subtracting it from resources dictionary.
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


# TODO 5: Calling function to start machine with while loop
is_on = True
#* While loop will run until user choice is "off"
while is_on:
    choice = input("What would you like? (espresso/Latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

