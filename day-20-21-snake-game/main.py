from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

little_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(little_snake.up, "Up")
screen.onkey(little_snake.down, "Down")
screen.onkey(little_snake.left, "Left")
screen.onkey(little_snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    little_snake.move(20)

    # Detect collision with food.
    if little_snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_up()
        little_snake.extend()

    # Detect collision with wall.
    if little_snake.head.xcor() > 280 or little_snake.head.xcor() < -280 or \
            little_snake.head.ycor() > 280 or little_snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    # if head collides with any segment in the tail
    for segment in little_snake.snake[1:]:
        if little_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
