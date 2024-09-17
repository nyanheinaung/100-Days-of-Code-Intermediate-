from turtle import Turtle
from ui import SCREEN_HEIGHT

ALIGNMENT = "center"
FONT = "Ariel"
FONT_SIZE = 20
FONT_TYPE = "normal"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.penup()
        self.goto(0, SCREEN_HEIGHT / 2 - FONT_SIZE * 2)
        self.display_score()

    def update_score(self, player):
        self.clear()
        if player:
            self.player_1_score += 1
        else:
            self.player_2_score += 1
        self.display_score()

    def display_score(self):
        self.write(f"SCORE : {self.player_1_score} - {self.player_2_score}",
                   False, ALIGNMENT, (FONT, FONT_SIZE, FONT_TYPE))
