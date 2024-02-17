from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.reset_position()

    def reset_position(self):
        x = 0
        y = -350
        self.goto(x, y)

    def move_right(self):
        new_x = self.xcor() + 10
        if self.xcor() > 280:
            new_x = 290
        self.setx(new_x)

    def move_left(self):
        new_x = self.xcor() - 10
        if self.xcor() < -280:
            new_x = -280
        self.setx(new_x)
