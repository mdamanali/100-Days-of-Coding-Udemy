"""
This is the Day 10 Project of 100 Days of Coding course from Udemy.
In this Project I have applied what I have learned on Day 10.
- Functions with Outputs
- Docstrings
"""

# Calculator

#? Add
def add(n1, n2):
    return n1+n2

#? Subtract
def subtract(n1, n2):
    return n1-n2

#? Multiply
def multiply(n1, n2):
    return n1*n2

#? Divide
def divide(n1, n2):
    return n1/ n2

#! Assigning function to symbols
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#? This is the main function which calculate.
def calculator():

    #! Take num1 from user
    num1 = float(input("What's the first number?: "))
    # Prints symbol from operations dictionary
    for symbol in operations:
        print(symbol)
    should_continue = True

    #? Used While loop to loop if user want to calcualte after getting answer.
    while should_continue:
        #! Takes operation from user
        operations_symbols = input ("Pick an operation: ")
        #! Takes num2 from the user
        num2 = float(input("What's the next numbers?: "))
        calculation_function = operations[operations_symbols]
        answer = calculation_function(num1, num2)

        #? This prints answers 
        print(f"{num1} {operations_symbols} {num2} = {answer}")
    
        #? This is the logic to continue if user want to continue
        if input(f"Type 'y' to continue calculating with {answer}, Or type 'n' to start a new calculation.: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()