from turtle import Turtle


class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("triangle")
        self.color("yellow")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.bullet_speed = 20
        self.bullet_speed2 = 10
        self.reload_interval = 0
        self.hideturtle()
        self.is_active = False
        self.set_position(5000, 5000)

    def set_position(self, x, y):
        self.goto(x, y)

    def move(self):
        if self.is_active:
            new_y = self.ycor() + self.bullet_speed
            self.sety(new_y)

    def enemy_fire(self):
        if self.is_active:
            new_y = self.ycor() - self.bullet_speed2
            self.sety(new_y)

    def check_collision(self, other):
        distance = self.distance(other)
        if distance < 15:
            return True
        return False

    def reload(self):
        self.reload_interval += 1
