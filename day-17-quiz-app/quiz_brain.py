class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        question_text = current_question.text
        question_answer = current_question.answer
        user_answer = input(f"Q.{self.question_number+1}: {question_text} (True/False) ")
        self.question_number += 1
        self.check_answer(user_answer, question_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Yeah! You are correct!")
            self.score += 1
        else:
            print("Opps! You are wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score: {self.score} / {self.question_number}")
        print("\n")



