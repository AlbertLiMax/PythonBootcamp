import turtle as t
import random

tim = t.Turtle()
tim.speed(0)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########


for i in range(0, 60):
    tim.color(random_color())
    tim.circle(200)
    tim.setheading(i * 6)

screen = t.Screen()
screen.exitonclick()
