from turtle import Turtle

SCORE_FONT = ("Ariel", 20, "normal")
GAME_OVER_FONT = ("Ariel", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = -1
        self.show_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.show_score()

    def show_score(self):
        self.write(f"Current Score: {self.score}", False, "center", SCORE_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", GAME_OVER_FONT)


