from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.goto(x=0, y=-330)
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.05
        
    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(x=new_x, y=new_y)
        
    def bounce(self, bounce_x, bounce_y):
        if bounce_x:
            self.move_x *= -1
        elif bounce_y:
            self.move_y *= -1
            
    def reset_position(self, x):
        self.goto(x=x, y=-330)
        self.bounce(bounce_x=False, bounce_y=True)
        
    def increase_speed(self):
        self.move_speed *= 0.7
        
    def game_over(self):
        self.hideturtle()
        