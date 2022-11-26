import turtle as t
from turtle import Screen as s

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
def dashed_line(length):
    tim.color("black")
    while length:
        tim.pendown()
        tim.forward(10)
        length -= 10
        print(length)
        if length:
            tim.penup()
            tim.forward(10)
            length -= 10
            print(length)

dashed_line(500)

screen = s()
screen.exitonclick()