from turtle import Turtle
STEP = 20


class Paddle():
    def __init__(self, x, y):
        self.body = [
            Turtle("square") for _ in range(3)
        ]
        for i in range(len(self.body)):
            self.body[i].hideturtle()
            self.body[i].speed("fastest")
            self.body[i].color("white")
            self.body[i].penup()
            self.body[i].goto(x=x, y=y+STEP-STEP*i)
            self.body[i].showturtle()

    def move_up(self):
        if self.body[0].ycor() >= 290:
            return
        for part in self.body:
            x, y = part.position()
            part.goto(x=x, y=y+STEP)

    def move_down(self):
        if self.body[-1].ycor() <= -280:
            return
        for part in self.body:
            x, y = part.position()
            part.goto(x=x, y=y-STEP)

    def is_colliding(self, obj):
        for i, part in enumerate(self.body):
            if part.distance(obj) < 15:
                return True
        return False

