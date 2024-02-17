from turtle import Turtle
import random
import time


FONT = ("Courier", 24, "normal")
FONT2 = ('Courier', 18, 'normal')
ALIGNMENT = "center"

def random_c():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.penup()
        self.color(random_c())
        self.user_prompt()
              
    def game_over(self, win):
        self.clear()
        self.goto(0, 0)
        if win == True:
            self.write("MODE {} COMPLETED. 🏆".format(self.current_level), align=ALIGNMENT, font=FONT)
            self.current_level += 1
            time.sleep(2)
        else:
            self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        
    def user_prompt(self):
        self.clear()
        self.goto(x=0, y=-330)
        self.write(f"MODE {self.current_level}", align=ALIGNMENT, font=FONT2)
        self.goto(x=0, y=-350)
        self.write("Press Space to PAUSE or RESUME the Game", align=ALIGNMENT, font=FONT2)
        
    def paused_status(self):
        self.clear()
        self.color(random_c())
        self.user_prompt()
        time.sleep(0.5)
