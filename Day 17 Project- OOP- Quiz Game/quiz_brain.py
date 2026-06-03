"""
This is the Main Brain of the Quizz Game
"""

#? This class (QuizBrain) is the brain of this project.
#? Where every thing like comparing questions, displaying questions, checking asnwer are there.
class QuizBrain:
    #* This initiallize the variables
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    #* This function (still_has_questions) is used to check if there is still question left in the list.
    def still_has_questions(self):
        # This returns True if question_number is less then length of the question_list
        return self.question_number < len(self.question_list)

    #* This function (next_question) is used to display questions and add 1 to question_number
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    #* This function (check_answer) is used to check answers of the question from data.py question_list
    def check_answer(self, user_answer, correct_answer):
        # if user_answer == to correct_answer it will add 1 to score variable.
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it Right!")
        # Else print("That's wrongs") and correct_answer, and current score of used
        else:
            print("That's wrong.")
        print(f"the correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

