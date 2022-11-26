###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(color_tuple)
#
# print(rgb_colors)

import turtle as t
import random as r

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def draw_dot(num):
    for i in range(num):
        tim.dot(20, r.choice(color_list))
        if i < num - 1:
            tim.forward(50)

tim = t.Turtle()
t.colormode(255)
tim.setheading(0)
tim.penup()
tim.hideturtle()
tim.speed(0)
for i in range(10):
    draw_dot(10)
    tim.home()
    tim.setheading(90)
    tim.forward(50 * (i + 1))
    tim.setheading(0)

screen = t.Screen()
screen.exitonclick()