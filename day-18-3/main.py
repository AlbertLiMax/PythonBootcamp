import turtle as t
from turtle import Screen as s
import random as r

tim = t.Turtle()
screen = s()

########### Challenge 3 - Draw Shapes ########
def draw_shape(gon_num):
    color = (r.randint(1, 255), r.randint(1, 255), r.randint(1, 255))
    screen.colormode(255)
    tim.pencolor(color)
    angle = 360 / gon_num
    for i in range(gon_num):
        tim.forward(100)
        tim.right(angle)

for i in range(3, 11):
    draw_shape(i)

screen.exitonclick()