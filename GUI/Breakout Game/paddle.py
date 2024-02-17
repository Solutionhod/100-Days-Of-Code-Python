from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.reset_position()
        
    def reset_position(self):
        x_pos = 0
        y_pos = -350
        self.goto(x_pos, y_pos)
        
    def left(self):
        if self.xcor() > -255:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())
        
    def right(self):
        if self.xcor() < 255:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())
            
    def game_over(self):
        self.hideturtle()