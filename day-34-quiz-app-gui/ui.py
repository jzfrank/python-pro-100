from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = Tk()
        self.root.title("Quizzler")
        self.root.configure(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(self.root, width=300, height=250, bg="white")
        self.canvas_text = self.canvas.create_text(
            150, 125, text="Some text",
            width=280,
            font=("Arial", 20, "italic"))

        self.score = 0
        self.score_label = Label(
            text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(
            image=right_image, highlightthickness=0, command=self.right_answered)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(
            image=wrong_image, highlightthickness=0, command=self.wrong_answered)

        self.canvas.grid(row=1, column=0, columnspan=2)
        self.score_label.grid(row=0, column=1, padx=10, pady=(10, 30))
        self.right_button.grid(row=2, column=0, padx=10, pady=(20, 0))
        self.wrong_button.grid(row=2, column=1, padx=10, pady=(20, 0))

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.right_button.config(state="active")
        self.wrong_button.config(state="active")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.canvas_text, text="You have reached the end of the quiz!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_answered(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def wrong_answered(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):

        self.score += 1
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.right_button.config(state="disabled")
        self.wrong_button.config(state="disabled")
        self.root.after(1000, self.get_next_question)
