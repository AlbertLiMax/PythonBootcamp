from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.level = 0

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.level += 1
        else:
            self.goto(self.xcor(), new_y)