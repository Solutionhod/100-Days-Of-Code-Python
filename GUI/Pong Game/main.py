from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from turtle import Screen
import time


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(x_bounce=False, y_bounce=True)
        
    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce(x_bounce=True, y_bounce=False)
        
    # detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        
    # detect when l_paddle misses 
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()