from turtle import Turtle

DISTANCE = 10

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = DISTANCE
        self.y_move = DISTANCE
        self.move_speed = 0.1
        
    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(x=new_x, y=new_y)
        
    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.x_move *= -1
            self.move_speed *= 0.9

        if y_bounce:
            self.y_move *= -1
            
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce(x_bounce=True, y_bounce=False)
        