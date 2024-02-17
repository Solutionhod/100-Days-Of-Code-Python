from ball import Ball
from bricks import Bricks
from paddle import Paddle
from scoreboard import Scoreboard
from turtle import Screen
from ui import UI
import time


screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)
screen.colormode(255)

paddle = Paddle()
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard(lives=5)
ui = UI()
game_paused = False
game_is_on = True


def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True      

def game_over():
    global game_is_on
    ball.game_over()
    paddle.game_over()
    bricks.game_over()
    scoreboard.game_over()
    ui.game_over(win=False)
    game_is_on = False

def wall_collision():
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce(bounce_x=True, bounce_y=False)   
    elif ball.ycor() > 350:
        ball.bounce(bounce_x=False, bounce_y=True)
        
def paddle_collision():
    if ball.distance(paddle) < 50 and ball.ycor() < -320:
        ball.bounce(bounce_x=False, bounce_y=True)       
    elif ball.ycor() < -380:
        ball.reset_position(paddle.xcor())
        scoreboard.decrease_lives()
        ui.change_color()

def brick_collision():
    for brick in bricks.bricks:       
        if ball.distance(brick) < 35:
            try:
                if ball.ycor() < brick.bottom_wall:
                    ball.bounce(bounce_x=False, bounce_y=True)
                elif ball.ycor() > brick.upper_wall:
                    ball.bounce(bounce_x=False, bounce_y=True)
                elif ball.xcor() < brick.left_wall:
                    ball.bounce(bounce_x=True, bounce_y=False)
                elif ball.xcor() > brick.right_wall:
                    ball.bounce(bounce_x=True, bounce_y=False)
            finally:
                brick.quantity -= 1
                if brick.quantity == 0:
                    brick.clear()
                    brick.goto(5000, 5000)
                    bricks.bricks.remove(brick)
                scoreboard.increase_score()
                
screen.listen()
screen.onkey(fun=paddle.left, key="Left")
screen.onkey(fun=paddle.right, key="Right")  
screen.onkey(fun=pause_game, key="space")  
    

while game_is_on:
    if not game_paused:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        wall_collision()
        paddle_collision()
        brick_collision()
        if len(bricks.bricks) == 0:
            ui.game_over(win=True)
            bricks.new_level()
            paddle.reset_position()
            ball.reset_position(paddle.xcor())
            ui.user_prompt()
            ball.increase_speed()
            game_is_on = True
        elif scoreboard.lives == 0:
            game_over()
    else:
        ui.paused_status()
    
screen.update()
screen.exitonclick()
