from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = []

def init_snake_body():
    for i in range(3):
        snake_body = Turtle()
        snake.append(snake_body)
        snake[i].shape("square")
        snake[i].color("white")
        snake[i].penup()
        snake[i].setpos(x=0-i*20, y=0)

init_snake_body()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for i in range(len(snake) - 1, 0, -1):
        new_x = snake[i - 1].xcor()
        new_y = snake[i - 1].ycor()
        snake[i].setpos(new_x, new_y)

    snake[0].forward(20)

screen.exitonclick()