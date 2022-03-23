from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    new_q = Question(question["text"], question["answer"])
    question_bank.append(new_q)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score} / {len(question_bank)}")