import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

tim = Turtle()

tim.shape("turtle")
tim.speed("fastest")
tim.hideturtle()

directions = [0, 90, 180, 270]

colors = [(236, 225, 215), (236, 225, 83), (202, 5, 72), (198, 164, 10), (235, 51, 129), (206, 76, 11), (108, 179, 218), (219, 162, 103), (234, 225, 6), (30, 188, 108), (23, 106, 173), (13, 23, 64), (17, 28, 175), (213, 135, 176), (9, 185, 214), (205, 29, 142), (229, 168, 197), (125, 189, 162), (8, 49, 28), (37, 132, 73), (125, 219, 233), (67, 22, 8), (61, 11, 26), (111, 89, 211), (142, 216, 201), (190, 15, 5), (238, 63, 31)]


def random_color(low=0, high=255):
    r = random.randint(low, high)
    g = random.randint(low, high)
    b = random.randint(low, high)
    return r, g, b


def draw_polygon(num_of_edges, length):

    degree = 180 - (num_of_edges - 2) * 180 / num_of_edges
    for i in range(num_of_edges):
        tim.forward(length)
        tim.right(degree)


def random_degree():
    return random.randint(0, 360)
    # return random.choice(directions)

x, y = -200, -200
tim.penup()

for i in range(10):
    y += 40
    tim.goto(x, y)
    for j in range(10):
        color = random_color(100, 255)
        tim.dot(20, color)
        tim.fd(40)








screen = Screen()
screen.exitonclick()