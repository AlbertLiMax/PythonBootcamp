from turtle import Turtle

LINE_LEN = 10
LINE_STEP = 15


class Table(Turtle):
    def __init__(self, length):
        super().__init__()
        # Draw middle line
        self.hideturtle()
        self.speed("fastest")
        self.pencolor("white")
        self.pensize(5)
        self.setheading(270)
        self.draw_middle_line(length)

    def draw_middle_line(self, length):
        self.penup()
        self.setpos(0, length / 2)
        for i in range(int(length / (LINE_LEN + LINE_STEP))):
            self.pendown()
            self.forward(LINE_LEN)
            self.penup()
            self.forward(LINE_STEP)
