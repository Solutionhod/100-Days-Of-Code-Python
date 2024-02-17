# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t
from random import choice

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
gap = 50
num_of_dots = 10

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(320)
tim.setheading(0)

def draw_dots():
    for _ in range(num_of_dots):
        tim.dot(20, choice(color_list))
        tim.forward(gap)
    tim.setheading(90)
    tim.forward(gap)
    tim.setheading(180)
    tim.forward(gap * num_of_dots)
    tim.setheading(0)
    
for _ in range(num_of_dots):
    draw_dots()
    
    
    




screen = t.Screen()
screen.exitonclick()