from turtle import Turtle

SCORE_POSITION = (0, 270)
FONT = ("Arial", 15, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(SCORE_POSITION)
        self.total_score = -1
        self.update_score()

    def update_score(self):
        self.clear()
        self.total_score += 1
        text = f"Score: {self.total_score}"
        self.write(text, False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)
