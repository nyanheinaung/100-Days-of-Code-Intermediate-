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
        self.total_score = 0

        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        text = f"Score: {self.total_score} High Score: {self.high_score}"
        self.write(text, False, ALIGNMENT, FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, ALIGNMENT, FONT)

    def reset(self):
        if self.total_score > self.high_score:
            self.high_score = self.total_score
            self.update_highscore()
        self.total_score = 0
        self.update_scoreboard()

    def update_highscore(self):
        with open("data.txt", "w") as data:
            data.write(str(self.high_score))
