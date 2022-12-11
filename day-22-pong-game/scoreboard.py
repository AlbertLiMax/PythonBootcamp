from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score_l}      {self.score_r}", align=ALIGNMENT, font=FONT)

    def score_up(self, left):
        if left:
            self.score_l += 1
        else:
            self.score_r += 1
        self.clear()
        self.update_scoreboard()
