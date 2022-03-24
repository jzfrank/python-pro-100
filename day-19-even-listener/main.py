from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                 prompt="which turtle will win the race? Enter a color")
print(user_bet)

colors = ["red", "green", "blue", "purple", "yellow", "pink", "gray"]
turtles = [None for color in colors]
for i, color in enumerate(colors):
    turtles[i] = Turtle()
    turtles[i].color(color)
    turtles[i].shape("turtle")
    turtles[i].penup()
    turtles[i].goto(x=-220, y=90 - i*30)

gameEnd = False
while not gameEnd:
    for i, t in enumerate(turtles):
        t.forward(random.randint(0, 5))
        if t.xcor() > 250:
            gameEnd = True
            print(f"Winner is: {t.pencolor()} turtle.")
            if t.pencolor() == user_bet:
                print("You are right!")
            else:
                print("You guessed wrong!")
            continue

screen.exitonclick()