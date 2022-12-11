from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(pos)

    def up(self):
        new_y = self.ycor() + 20
        self.setpos(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.setpos(self.xcor(), new_y)
