from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.heading = 0

    def create_snake(self):
        for i in range(3):
            snake_body = Turtle("square")
            self.snake.append(snake_body)
            self.snake[i].color("white")
            self.snake[i].penup()
            self.snake[i].setpos(x=0 - i * 20, y=0)
#        self.head = self.snake[0]

    def move(self, distance):
        time.sleep(0.1)

        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].setpos(new_x, new_y)

        self.head.forward(distance)

    def up(self):
        self.heading = self.head.heading()
        if self.heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        self.heading = self.head.heading()
        if self.heading != UP:
            self.head.setheading(DOWN)

    def left(self):
        self.heading = self.head.heading()
        if self.heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        self.heading = self.head.heading()
        if self.heading != LEFT:
            self.head.setheading(RIGHT)
