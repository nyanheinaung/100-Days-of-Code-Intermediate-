from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from gamemanager import GameManager
import time
# import random


screen = Screen()
screen.screensize(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
game_manager = GameManager()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
next_stage = True

while game_is_on:
    time.sleep(game_manager.sleep_time)

    if next_stage:
        # screen.clearscreen()
        game_manager.next_stage()
        scoreboard.increase_score()
        next_stage = False

    if player.ycor() >= 280:
        next_stage = True
        player.reset_position()

    if game_manager.check_collision(player):
        game_is_on = False
        screen.clearscreen()
        scoreboard.game_over()

    screen.update()

screen.exitonclick()
