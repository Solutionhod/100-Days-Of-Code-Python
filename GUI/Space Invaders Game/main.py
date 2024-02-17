from bullet import Bullet
from enemies import Enemies
from player import Player
from scoreboard import Scoreboard
from turtle import Screen
from ui import UI
import time

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.tracer(0)
screen.colormode(255)

player = Player()
enemies = Enemies()
bullet = Bullet()
enemy_bullet = Bullet()
ui = UI()
scoreboard = Scoreboard(3)
game_paused = False
game_is_on = True


def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True


def fire_bullet():
    if not bullet.is_active:
        bullet.is_active = True
        x = player.xcor()
        y = player.ycor()
        bullet.set_position(x, y)
        bullet.showturtle()


def enemy_fire(enemy):
    if not enemy_bullet.is_active:
        enemy_bullet.is_active = True
        x = enemy.xcor()
        y = enemy.ycor()
        enemy_bullet.set_position(x, y)
        enemy_bullet.showturtle()


def check_collisions():
    global game_is_on
    for enemy in enemies.enemies:
        if bullet.check_collision(enemy):
            bullet.hideturtle()
            bullet.goto(5000, 5000)
            bullet.is_active = False
            enemy.hideturtle()
            if enemy.enemy_power == 1:
                scoreboard.increase_a()
            elif enemy.enemy_power == 2:
                scoreboard.increase_b()
            else:
                scoreboard.increase_c()
            enemies.enemies.remove(enemy)
            scoreboard.update_score()

        elif enemy.ycor() < -320:
            ui.game_over(win=False)
            game_is_on = False

        elif enemy.xcor() == player.xcor():
            enemy_bullet.reload()
            if enemy_bullet.reload_interval % 5 == 0:
                enemy_fire(enemy)

        elif enemy_bullet.check_collision(player):
            enemy_bullet.hideturtle()
            enemy_bullet.goto(5000, 5000)
            enemy_bullet.is_active = False
            player.reset_position()
            ui.change_color()
            scoreboard.decrease_lives()

        elif enemy_bullet.ycor() < -400:
            enemy_bullet.hideturtle()
            enemy_bullet.goto(5000, 5000)
            enemy_bullet.is_active = False

    if bullet.ycor() > 360:
        bullet.hideturtle()
        bullet.goto(5000, 5000)
        bullet.is_active = False


screen.listen()
screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=fire_bullet, key="space")
screen.onkey(fun=pause_game, key="s")

while game_is_on:
    if not game_paused:
        time.sleep(0.01)
        screen.update()
        enemies.move_enemies()
        bullet.move()
        enemy_bullet.enemy_fire()
        check_collisions()
        if len(enemies.enemies) == 0:
            ui.game_over(win=True)
            enemies.new_level()
            player.reset_position()
            ui.user_prompt()
            game_is_on = True

        elif scoreboard.lives == 0:
            scoreboard.reset_score()
            ui.game_over(win=False)
            game_is_on = False

    else:
        ui.paused_status()

screen.exitonclick()
