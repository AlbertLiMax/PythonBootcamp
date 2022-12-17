from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(0, 280)
        self.update_scoreboard()

    def read_high_score(self):
        with open("score.txt") as file:
            self.high_score = int(file.read())

    def update_high_score(self):
        with open("score.txt", mode="w") as file:
          file.write(f"{self.high_score}")

    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.clear()
        self.update_scoreboard()

#    def game_over(self):
#        self.clear()
#        self.update_scoreboard()
#        self.setpos(0, 0)
#        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
