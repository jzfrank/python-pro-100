from turtle import Turtle
import random
STEP = 10


class PongBall(Turtle):
    def __init__(self):
        super(PongBall, self).__init__()
        self.shape("circle")
        self.color('white')
        self.speed("fastest")
        self.shapesize(0.8, 0.8)
        self.penup()
        self.cnt = 0
        self.rethrow()
        self.move_speed = 0.1

    def rethrow(self):
        self.move_speed = 0.1
        self.goto(x=0, y=0)
        if self.cnt % 2 == 0:
            self.setheading((random.randint(-60, 60) + 360) % 360)
        else:
            self.setheading(random.randint(120, 240))
        self.cnt += 1

    def move(self):
        self.forward(STEP)

    def bounce_vertical(self):
        print("bounce vertical")
        print(self.heading())
        heading = self.heading()
        new_heading = (540 - heading) % 360
        self.setheading(new_heading)
        print(self.heading())

        self.move_speed *= 0.9

        self.move()

    def bounce_horizontal(self):
        print("bounce horizontal")
        print(self.heading())
        heading = self.heading()
        new_heading = (720 - heading) % 360
        self.setheading(new_heading)
        print(self.heading())

        # self.move_speed *= 0.9

        self.move()

