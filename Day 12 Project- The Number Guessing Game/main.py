"""
This is the Day 12 Project of 100 Days of Coding Course from Udemy.
In this Project I have applied what I have learned on Day 12
- Global Scope
- Local Scope
"""

from random import randint
from art import logo

#! Global Scope
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#? Function to check users' guess against actual answer
#* It used IF and ELSE statement to check users against the actual answer
def check_answer(user_guess, actual_answer, turns):
    """Check answer agianst guess, returns the number of turns remaining."""
    # If user guess is higher then actual answer. Then print "Too high".
    #! And also subtract the turns users have for guessing
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    # If user guess is lower then actual answer. Then print "Too low"
    #! And also subtract the turns users have for guessing
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    # If user guess is equal to actual answer. Then print statement below
    else:
        print(f"You got it! The answer was {actual_answer}")


#? Function to set difficulty.
#* This function set the difficulty by calling GLOBAL SCOPE.
def set_difficulty():
    # Input from user for easy and hard level
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    #! If user input is 'easy' then level will be set to EASY_LEVEL_TURNS. which is 10 turns for guessing
    if level == 'easy':
        return EASY_LEVEL_TURNS
    #! Else user input is 'hard' then level will be set to HARD_LEVEL_TUENS. which is 5 turns for guessing.
    else:
        return HARD_LEVEL_TURNS
    
 
#? This is the Main Function of the Game.
#* This function is User Interface in Terminal
def game():
    # Prints Logo from art.py module
    print(logo)

    # Prints Welcome statements
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    #! This is the actual answer randomely taken from between 1 to 100.
    answer = randint(1, 100)
    
    #! This sets turn according to user input by calling set_difficulty() function
    turns = set_difficulty()

    #! While loop for looping and asking user to guess the answer.
    #* IF the guess is not equal to answer then repeat.
    #* If guess is equal to answer then print statement from check_answer() function.
    guess = 0
    while guess != answer:
        #? Print how many turns are left from set_difficulty() function.
        print(f"You have {turns} attempts remaining to guess the number.")

        #* Guess input from user
        guess = int(input("Make a guess: "))

        #! This Give you how many turns are remaining.
        turns = check_answer(guess, answer, turns)
        # IF turns equals to 0. Then print you lose and actal answer
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"Pssst, the correct answer is {answer}")
            return
        elif guess != answer:
            print("Guess again.")

game()