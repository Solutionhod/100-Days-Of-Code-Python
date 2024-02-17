from turtle import Turtle
from ui import random_c


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
COLOR = "white"


class Snake(Turtle):
    
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color(COLOR)
        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(random_c())
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
  
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  
        self.head.forward(MOVE_DISTANCE)
            
    def barrier(self, barrier_x, barrier_y):
        if barrier_x:
            new_x = self.head.xcor()
            self.head.setx(new_x * -1) 
        elif barrier_y:
            new_y = self.head.ycor()
            self.head.sety(new_y * -1) 
                      
    def game_over(self):
        for segment in self.segments:
            segment.hideturtle()
            
    def reset_snake(self):
        for segment in self.segments:
            segment.clear()
            segment.goto(5000, 5000)
            self.segments.remove(segment)
        self.create_snake()       
        self.head = self.segments[0]
        self.head.color(COLOR)
                
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)   
    