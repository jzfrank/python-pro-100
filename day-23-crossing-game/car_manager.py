from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

SCREEN_HEIGHT = 600


class CarManager:
    def __init__(self):
        self.cars = [
            [] for i in range(SCREEN_HEIGHT // MOVE_INCREMENT)
        ]
        self.speed = STARTING_MOVE_DISTANCE

    def add_cars(self):
        # if random.randint(1, 6) != 1:
        #     return
        i = random.randint(0, len(self.cars)-1)
        new_car = Turtle("square")
        new_car.penup()
        new_car.turtlesize(1, 2)
        new_car.color(random.choice(COLORS))
        if len(self.cars[i]) == 0:
            nx = 280
        else:
            nx = 300
        ny = -280 + 3*MOVE_INCREMENT*i
        new_car.goto(x=nx, y=ny)
        self.cars[i].append(new_car)

    def move_cars(self):
        for j, row in enumerate(self.cars):
            for i in range(len(row)-1, -1, -1):
                car = row[i]
                car.setx(car.xcor() - self.speed)
                if car.xcor() <= -280:
                    car.reset()
                    car.hideturtle()
                    self.cars[j] = row[i+1:]
                    break

    def is_colliding(self, player):
        for row in self.cars:
            for car in row:
                # if car.distance(player) < 20:
                if abs(car.xcor() - player.xcor()) < 30 and abs(car.ycor() - player.ycor()) < 15:
                    return True
        return False

    def level_up(self):
        self.speed *= 1.5
        for row in self.cars:
            for car in row:
                car.reset()
                car.hideturtle()
        self.cars = [
            [] for i in range(SCREEN_HEIGHT // MOVE_INCREMENT)
        ]


