import random
from turtle import Turtle


try:
	SCORE = int(open("highestscore.txt", "r").read())
except FileNotFoundError:
	SCORE = open("highestscore.txt", "w").write(str(0))
except ValueError:
    SCORE = 0

FONT = ("Courier", 18, "normal")
FONT2 = ("Courier", 14, "normal")
ALIGNMENT = "center"
COLOR = "white"


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.score = 0
        self.highscore = SCORE
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(x=0, y=320)
        self.write("Score: {} | High Score: {}".format(self.score, self.highscore), align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
        self.update_scoreboard()
        
    def game_over(self):
        self.clear()
        self.goto(0, -100)
        self.write("FINAL SCORE: {} | HIGHEST SCORE: {}".format(self.score, self.highscore), align=ALIGNMENT, font=FONT)
        open("highestscore.txt", "w").write(str(self.highscore))
    