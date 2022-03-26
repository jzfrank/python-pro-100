from turtle import Turtle, Screen
from paddle import Paddle
from pongball import PongBall
from scoreboard import ScoreBoard
import time


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) # turn off animation
screen.title("Pong Game")

paddle1 = Paddle(-290, 0)
paddle2 = Paddle(280, 0)
scoreboard = ScoreBoard()
pongball = PongBall()

tim = Turtle()
tim.hideturtle()
tim.color("white")
tim.penup()
tim.goto(0, 290)
tim.setheading(270)
for i in range(300):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

time.sleep(0.1)
screen.update()

screen.listen()
screen.onkey(key="w", fun=paddle1.move_up)
screen.onkey(key="s", fun=paddle1.move_down)
screen.onkey(key="Up", fun=paddle2.move_up)
screen.onkey(key="Down", fun=paddle2.move_down)

gameIsOn = True

while gameIsOn:
    scoreboard.display()
    screen.update()
    pongball.move()
    # detect collision with the upper/lower wall
    if abs(pongball.ycor()) > 285:
        print("collide with wall")
        pongball.bounce_horizontal()

    # detect fail to capture of ball
    if abs(pongball.xcor()) > 290:
        print("lose the ball...")
        if pongball.xcor() > 290:
            print("paddle2 lose the ball")
            scoreboard.increase_score("left")
        else:
            print("paddle1 lose the ball")
            scoreboard.increase_score("right")
        pongball.rethrow()
        time.sleep(0.5)
        continue

    # detect collision with the board
    if paddle1.is_colliding(pongball):
        print("collided with paddle1")
        pongball.bounce_vertical()
    elif paddle2.is_colliding(pongball):
        print("collided with paddle2")
        pongball.bounce_vertical()

    time.sleep(pongball.move_speed)


screen.exitonclick()
