import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_cars(self):
        new_car = Turtle("square")
        new_car.shape("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.goto(random.uniform(-300, 300), random.uniform(-200, 240))
        self.all_cars.append(new_car)

    def move(self, level):
        for car in self.all_cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE - level * MOVE_INCREMENT
            if new_x < -320:
                car.goto(320, random.uniform(-200, 240))
            else:
                car.goto(new_x, car.ycor())