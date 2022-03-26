from turtle import Turtle

STARTING_POSITIONS = [(40, 0), (20, 0), (0, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(len(STARTING_POSITIONS)):
            self.add_segment(STARTING_POSITIONS[i])

    def add_segment(self, position):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        x, y = position
        snake_body.goto(x=x, y=y)
        self.segments.append(snake_body)

    def extend(self):
        self.add_segment(self.segments[-1].pos())
        print([self.segments[i].pos() for i in range(len(self.segments))])

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
