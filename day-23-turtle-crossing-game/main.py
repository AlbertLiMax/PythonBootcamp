import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

delay = [0.1, 0.2, 0.3, 0.4, 0.5]

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

cars = CarManager()
for i in range(15):
    cars.create_cars()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # Update the level.
    scoreboard.update_scoreboard(player.level)

    # Moving cars.
    cars.move(player.level)
    for i in range(15):
        # Detect collision with cars.
        if player.distance(cars.all_cars[i]) < 25:
            scoreboard.game_over()
            game_is_on = False
            break

    screen.update()

screen.exitonclick()