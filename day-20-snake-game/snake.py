from turtle import Turtle
import time

class Snake():
    def __init__(self):
        self.snake = []
        for i in range(3):
            snake_body = Turtle("square")
            self.snake.append(snake_body)
            self.snake[i].color("white")
            self.snake[i].penup()
            self.snake[i].setpos(x=0 - i * 20, y=0)


    def move(self, distance):
        time.sleep(0.1)

        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].setpos(new_x, new_y)

        self.snake[0].forward(distance)

    def turn(self, degree):
        self.snake[0].right(degree)