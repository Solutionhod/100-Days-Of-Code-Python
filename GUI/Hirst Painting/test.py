from random import choice, randint
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.colormode(255)

# colors = ["blue violet", "brown", "CadetBlue", "coral", "dark orange", "blue", "DarkKhaki", "red", "green", "yellow", "greenyellow", "black", "green"]
# # Draw different shapes
# def draw(shape):
#     for _ in range(shape):
#         tim.right(360/shape)
#         tim.forward(100)

# for shape in range(3, 11):
#     tim.color(choice(colors))
#     draw(shape)


# # Generate random walks
# direction = [0, 90, 180, 270]
# distance = 50

# def draw():
#     tim.speed("fastest")
#     tim.pensize(20)
#     tim.color(choice(colors))
#     tim.right(choice(direction))
#     tim.forward(distance)

# for _ in range(300):
#     draw()


# # Generate random rgb colors
# direction = [0, 90, 180, 270]
# distance = 30
# tim.speed("fastest")
# tim.pensize(15)

# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return (r, g, b)

# for _ in range(300):
#     tim.color(random_color())
#     tim.forward(distance)
#     tim.setheading(choice(direction))


# Draw a spirograph
radius = 100
tim.speed("fastest")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def spirograph(turns):
    for _ in range(turns):
        tim.color(random_color())
        tim.circle(radius)
        tim.setheading(tim.heading() + 360/turns)
        tim.circle(radius)
        
        
spirograph(100)
    


screen.exitonclick()