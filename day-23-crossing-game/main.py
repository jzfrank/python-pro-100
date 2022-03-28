import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
print(scoreboard.level)

screen.listen()
screen.onkey(key="Up", fun=player.up)
cnt = 0

game_is_on = True
while game_is_on:
    cnt += 1
    scoreboard.display()
    # generate cars randomly
    car_manager.add_cars()
    car_manager.move_cars()
    # detect collision with cars
    if car_manager.is_colliding(player):
        scoreboard.game_over()
        game_is_on = False
        print("game over")
    if player.reached_final():
        print("reached final")
        player.restart()
        car_manager.level_up()
        scoreboard.level_up()
        continue
    time.sleep(0.1)
    screen.update()


screen.exitonclick()