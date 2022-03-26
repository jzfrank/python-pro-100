from turtle import Turtle
FONT = ("Courial", 20, 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = {
            'left': 0,
            'right': 0
        }
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.display()

    def display(self):
        self.clear()
        self.write(f"{self.score['left']} : {self.score['right']}",
                   align = 'center', font=FONT)

    def increase_score(self, player):
        self.score[player] += 1