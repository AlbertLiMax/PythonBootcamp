from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def bounce(self, x):
        if x == 1:
            self.x_move *= -1
        else:
            self.y_move *= -1

    def reset(self):
        self.setpos(0, 0)
        self.bounce(1)
