from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

position = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.heading = 0

    def create_snake(self):
        for i in range(3):
            self.add_segment(position[i])

    def add_segment(self, pos):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.setpos(pos)
        self.snake.append(snake_body)

    def extend(self):
        self.add_segment(self.snake[-1].position())

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
