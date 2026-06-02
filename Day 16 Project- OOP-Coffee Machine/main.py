"""
This is the main module where all the piece joins.
"""

#! Importing the classes from the modules
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#! Creating Objects from the class
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

#? Looping through the coffee making process until is_on is False
is_on = True

while is_on:
    #* Getting the optiosn from Menu class inside menu.py
    options = menu.get_items()
    #* Printing the options and letting users choose the Drink
    choice = input(f"What would you like? ({options}): ")
    #* If choice of user == 'off' then Coffee Machine will turn off
    if choice == "off":
        is_on = False
    #* Elif choice of user == 'report' then print the profit from money_machine.py and resources from menu.py
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    #* Else make coffee if resources and money used gave is sufficient
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
