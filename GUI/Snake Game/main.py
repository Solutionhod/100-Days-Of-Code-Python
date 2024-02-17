from food import Food
from gamemode import GameMode
from scoreboard import Scoreboard
from snake import Snake
from ui import UI
import time
import turtle


mode = int(turtle.textinput("Choose Game Mode", f"Select Number\n--0-- for Classic\n--1-- for Mode 1\n--2-- for Mode 2\n--3-- for Mode 3\n--4-- for Mode 4\n--5-- for Mode 5"))
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.colormode(255)
tim = turtle.Turtle()
tim.penup()
tim.color("white")
tim.goto(-300, -300)
tim.pendown()
for i in range(4):
    tim.forward(600)
    tim.left(90)
tim.hideturtle()

snake = Snake()
food = Food()
scoreboard = Scoreboard()
gamemode = GameMode(mode)
ui = UI()

game_is_on = True
game_is_paused = False

def pause_game():
    global game_is_paused
    if game_is_paused:
        game_is_paused = False
    else:
        game_is_paused = True
        
def game_over():
    global game_is_on
    snake.game_over()
    food.game_over()
    gamemode.game_over()
    scoreboard.game_over()
    ui.game_over(win=False)
    game_is_on = False
    
def is_obstacle_collision():
    for obstacle in gamemode.obstacles:
        if snake.head.distance(obstacle) < 15:
            game_over()
                  
def is_tail_collision():
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over()
            
def is_wall_collision():
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        snake.barrier(barrier_x=True, barrier_y=False)
    elif snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.barrier(barrier_x=False, barrier_y=True)
        
def is_food_collision():
    if snake.head.distance(food) < 15:
        food.refresh()
        for obstacle in gamemode.obstacles: 
            if obstacle.position() == food.position():
                food.refresh()
        snake.extend() 
        scoreboard.increase_score()
        
def is_classic_mode():
    if gamemode.classic_mode == True:
        if gamemode.mode == 6:
            game_over()               
        elif len(snake.segments) == 30:
            ui.game_over(win=True)
            gamemode.next_mode()
            snake.reset_snake()
            ui.user_prompt()       
                    
            
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(pause_game, "space")

while game_is_on:
    if not game_is_paused:
        screen.update()
        time.sleep(0.1)
        snake.move()
        is_food_collision()
        is_obstacle_collision()
        is_tail_collision()
        is_wall_collision()
        is_classic_mode()
    else:
        ui.paused_status()
        
screen.update()
screen.exitonclick()
