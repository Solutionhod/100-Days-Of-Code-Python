from turtle import Turtle
import random
import ui

WEIGHTS = [1, 1, 1, 1, 1, 1, 1]

class Brick(Turtle):
    
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=2.05)
        # self.color()
        self.color(ui.random_c())
        self.goto(x=x_cor, y=y_cor)
        self.quantity = random.choice(WEIGHTS)
        # Defining borders of the brick
        self.left_wall = self.xcor() - 24
        self.right_wall = self.xcor() + 24
        self.upper_wall = self.ycor() + 20
        self.bottom_wall = self.ycor() - 20
        
        
class Bricks():
    
    def __init__(self):
        self.y_start = 300
        self.bricks = []
        self.level = 0
        self.new_level()

    def create_lane(self, y_cor):
        self.bricks += [Brick(i, y_cor) for i in range(-280, 290, 42)]

    def create_all_lanes(self):
        if self.level <= 5:
            y_end = self.y_start - self.level*31
            WEIGHTS.append(2)
        elif self.level > 5 and self.level <= 10:
            y_end = self.y_start - self.level*35
            WEIGHTS.append(3)
        else:
            y_end = -60
            WEIGHTS.append(4)       
        for i in range(self.y_start, y_end, -31):
            self.create_lane(i)
    
    def new_level(self):
        self.level += 1
        self.create_all_lanes()
        
    def game_over(self):
        for brick in self.bricks:
            brick.hideturtle()