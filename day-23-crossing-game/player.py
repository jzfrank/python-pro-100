from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.restart()

    def restart(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def reached_final(self):
        return self.ycor() >= FINISH_LINE_Y



