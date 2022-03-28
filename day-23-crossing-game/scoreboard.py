from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=270)
        self.speed("fastest")
        self.level = 0

    def display(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over", align="center", font=FONT)
