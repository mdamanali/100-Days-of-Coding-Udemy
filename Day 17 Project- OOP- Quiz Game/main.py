
#! Importing class, list from other modules
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#* Created empty list.
question_bank = []
#* Looping through the question_data from data.py module.
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # This sets the question_text from the data into Question class
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

#* looping through the still_has_question()
while quiz.still_has_questions():
    # Calling next_question function until there is no more questions left
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")