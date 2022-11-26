import turtle as t
import random as r
from turtle import Screen

tim = t.Turtle()
tim.pensize(20)
########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "Yellow", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angle = [90, 180, 270, 360]
screen = Screen()
tim.speed(0)

for i in range(300):
    tim.color(r.choice(colours))
    tim.forward(30)
    tim.setheading(r.choice(angle))

screen.exitonclick()