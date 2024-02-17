from turtle import Turtle

try:
    SCORE = int(open("highestscore.txt", "r").read())
except FileNotFoundError:
    SCORE = open("highestscore.txt", "w").write(str(0))
except ValueError:
    SCORE = 0

FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self, lives):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = lives
        self.score = 0
        self.highscore = SCORE
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-250, y=360)
        self.write(f"Score: {self.score} | Highest Score: {self.highscore}",
                   align="left",
                   font=FONT)
        self.goto(x=250, y=360)
        self.write(f"Lives: {self.lives}", align="right", font=FONT)

    def increase_a(self):
        self.score += 10
        if self.score > self.highscore:
            self.highscore = self.score

    def increase_b(self):
        self.score += 20
        if self.score > self.highscore:
            self.highscore = self.score

    def increase_c(self):
        self.score += 30
        if self.score > self.highscore:
            self.highscore = self.score

    def decrease_lives(self):
        self.lives -= 1
        self.update_score()

    def reset_score(self):
        self.clear()
        self.score = 0
        self.update_score()
        open("highestscore.txt", "w").write(str(self.highscore))
