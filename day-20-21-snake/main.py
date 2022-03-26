from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

scoreboard = Scoreboard()
scoreboard.display()

food = Food()
gameIsOn = True
while gameIsOn:
    screen.update()
    snake.move()
    time.sleep(0.1)
    # detect collision
    if snake.head.distance(food) < 15:
        print("food and snake collides")
        snake.extend()
        food.refresh()
        scoreboard.incr_score()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        gameIsOn = False
        print("game over because collision with wall")
        scoreboard.game_over()

    # detect collision with tail
    # if head collides with any segment in the tail:
    #    trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameIsOn = False
            print("game over because collision with tail")
            scoreboard.game_over()




screen.exitonclick()

