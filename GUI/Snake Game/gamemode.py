from turtle import Turtle
import time


class Obstacle(Turtle):
    
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.goto(x, y)


class GameMode():
    
    def __init__(self, mode):
        self.obstacles = []
        self.mode = mode
        self.classic_mode = False
        self.create_mode()
        
    def create_mode(self):
        if self.mode == 1:
            return None
        elif self.mode == 2:
            self.obstacles += [Obstacle(i, 200) for i in range(-150, 151, 10)]
            self.obstacles += [Obstacle(i, -200) for i in range(-150, 151, 10)]
        elif self.mode == 3:
            self.obstacles += [Obstacle(-200, i) for i in range(-200, -101, 10)]
            self.obstacles += [Obstacle(-200, i) for i in range(200, 101, -10)]
            self.obstacles += [Obstacle(200, i) for i in range(-200, -101, 10)]
            self.obstacles += [Obstacle(200, i) for i in range(200, 101, -10)]
            self.obstacles += [Obstacle(i, -200) for i in range(-200, -101, 10)]
            self.obstacles += [Obstacle(i, -200) for i in range(200, 101, -10)]
            self.obstacles += [Obstacle(i, 200) for i in range(-200, -101, 10)]
            self.obstacles += [Obstacle(i, 200) for i in range(200, 101, -10)]
        elif self.mode == 4:
            self.obstacles += [Obstacle(i, 160) for i in range(-150, 151, 10)]
            self.obstacles += [Obstacle(i, -160) for i in range(-150, 151, 10)]
            self.obstacles += [Obstacle(-295, i) for i in range(-295, -201, 10)]
            self.obstacles += [Obstacle(-295, i) for i in range(295, 201, -10)]
            self.obstacles += [Obstacle(295, i) for i in range(-295, -201, 10)]
            self.obstacles += [Obstacle(295, i) for i in range(295, 201, -10)]
            self.obstacles += [Obstacle(i, -295) for i in range(-295, -201, 10)]
            self.obstacles += [Obstacle(i, -295) for i in range(295, 201, -10)]
            self.obstacles += [Obstacle(i, 295) for i in range(-295, -201, 10)]
            self.obstacles += [Obstacle(i, 295) for i in range(295, 201, -10)]            
        elif self.mode == 5:
            self.obstacles += [Obstacle(-300, i) for i in range(-300, 301, 10)]
            self.obstacles += [Obstacle(300, i) for i in range(-300, 301, 10)]
            self.obstacles += [Obstacle(i, 300) for i in range(-300, 301, 10)]
            self.obstacles += [Obstacle(i, -300) for i in range(-300, 301, 10)]
        else:
            self.classic()
            
    def classic(self):
        if self.classic_mode == False:
            self.mode = 1
            self.classic_mode = True
            self.create_mode()
            
    def next_mode(self):
        for obstacle in self.obstacles:
            obstacle.clear()
            obstacle.goto(5000, 5000)
        self.mode += 1
        time.sleep(2)
        self.create_mode()
        
    def game_over(self):
        for obstacle in self.obstacles:
            obstacle.hideturtle()
            