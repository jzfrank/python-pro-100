import turtle
import pandas as pd
FONT = ("Courier", 14, "normal")


states_data = pd.read_csv("50_states.csv")
print(states_data.head())
states = states_data["state"].tolist()


screen = turtle.Screen()
screen.title("U.S. States game")

image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


screen.listen()
screen.onscreenclick(lambda x, y: print(f"x: {x}, y: {y}"))
screen.tracer(0) # no animation

tim = turtle.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()

guessed_states = set()

while len(guessed_states) < 50:
    screen.update()
    answer_state = screen.textinput(
        title=f"{len(guessed_states)} / 50 states correct",
        prompt="What is another state's name?")
    print(answer_state)
    if not answer_state or answer_state == "exit":
        break
    answer_state = answer_state.capitalize()
    if answer_state in states:
        guessed_states.add(answer_state)
        x = states_data[states_data["state"] == answer_state]['x']
        y = states_data[states_data["state"] == answer_state]['y']
        x = float(x)
        y = float(y)
        tim.goto(x, y)
        tim.write(answer_state, align="Center", font=FONT)

states_data[states_data.state.apply(
    lambda x: x not in guessed_states)].\
    to_csv("missed_cities.csv")


turtle.mainloop()

