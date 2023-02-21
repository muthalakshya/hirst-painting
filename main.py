# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r,g,b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)

from turtle import Turtle , Screen
import random

spot = Turtle()
screen = Screen()

screen.colormode(255)
spot.hideturtle()
color = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
 (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
 (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
 (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

for i in range(10):
    m = i * 50
    spot.penup()
    spot.setposition(-300 ,-300 + m )
    spot.pendown()

    for _ in range(10):
        # spot.fillcolor(random.choice(color))
        spot.begin_fill()
        # spot.circle(10)
        spot.dot(20,random.choice(color))
        spot.end_fill()
        spot.penup()
        spot.forward(50)
        spot.speed("fastest")
        spot.pendown()

screen.exitonclick()