from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.score = 0

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def incr_score(self):
        self.score += 1
        self.display()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)