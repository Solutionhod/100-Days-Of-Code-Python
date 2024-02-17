from turtle import Turtle


class Enemy(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.goto(x, y)
        self.setheading(270)
        self.enemy_power = 0


class Enemies:

    def __init__(self):
        self.y_start = 300
        self.enemies = []
        self.enemy_speed = 0
        self.new_level()

    def create_enemies(self):
        self.enemies += [
            Enemy(x, y) for y in range(300, 100, -50)
            for x in range(-200, 201, 55)
        ]
        for enemy in self.enemies[:8]:
            enemy.color("red")
        for enemy in self.enemies[8:16]:
            enemy.color("blue")
            enemy.enemy_power = 2
        for enemy in self.enemies[16:32]:
            enemy.color("purple")
            enemy.enemy_power = 1

    def move_enemies(self):
        for enemy in self.enemies:
            new_x = enemy.xcor() + self.enemy_speed
            enemy.setx(new_x)
            if enemy.xcor() > 280 or enemy.xcor() < -280:
                self.enemy_speed *= -1
                for i in self.enemies:
                    new_y = i.ycor() - 20
                    i.sety(new_y)

    def new_level(self):
        self.enemy_speed += 0.5
        self.create_enemies()
