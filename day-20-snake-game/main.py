from snake import Snake
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

little_snake = Snake()

screen.listen()
screen.onkey(little_snake.up, "Up")
screen.onkey(little_snake.down, "Down")
screen.onkey(little_snake.left, "Left")
screen.onkey(little_snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    little_snake.move(20)

screen.exitonclick()
