from turtle import Screen
from table import Table
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

table = Table()
table.draw_middle_line(600)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()

    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Need to bounce
        ball.bounce(0)

    # Detect collision with paddle.
    if ball.distance(paddle_r) < 20 and ball.xcor() > 320 \
            or ball.distance(paddle_l) < 20 and ball.xcor() < -320:
        ball.bounce(1)

    # Detect paddle miss
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.score_up(1)
    elif ball.xcor() < -400:
        ball.reset()
        scoreboard.score_up(0)

    screen.update()

screen.exitonclick()
