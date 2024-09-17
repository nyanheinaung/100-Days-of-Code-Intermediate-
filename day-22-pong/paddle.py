from turtle import Turtle
from ui import SCREEN_WIDTH, SCREEN_HEIGHT

PADDLE_LENGTH = 4
PADDLE_SPEED = 50
LIMIT = SCREEN_HEIGHT/2 - 20 * PADDLE_LENGTH/2


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.hideturtle()
        self.penup()
        if player == 1:
            x_pos = 30 - SCREEN_WIDTH // 2
        else:
            x_pos = SCREEN_WIDTH // 2 - 30
        self.goto(x_pos, 0)
        self.paddle = []
        self.create_paddle(player)

    def create_paddle(self, player):
        for i in range(PADDLE_LENGTH):
            p = Turtle()
            p.shape("square")
            p.penup()
            p.color("white")

            if player == 1:
                x_pos = 30 - SCREEN_WIDTH // 2
            else:
                x_pos = SCREEN_WIDTH // 2 - 30

            if PADDLE_LENGTH & 1:
                y_pos = -20 * PADDLE_LENGTH//2 + 20*i
            else:
                y_pos = -20 * PADDLE_LENGTH//2 + 20*i + 10

            p.goto(x_pos, y_pos)
            self.paddle.append(p)

    def move_up(self):
        if self.ycor() < LIMIT:
            if self.ycor() + PADDLE_SPEED > LIMIT:
                y_increment = self.ycor() + PADDLE_SPEED - LIMIT
            else:
                y_increment = PADDLE_SPEED
            self.sety(self.ycor() + y_increment)
            for p in self.paddle:
                p.sety(p.ycor() + y_increment)

    def move_down(self):
        if self.ycor() > -LIMIT:
            if self.ycor() - PADDLE_SPEED < -LIMIT:
                y_increment = self.ycor() - PADDLE_SPEED + LIMIT
            else:
                y_increment = PADDLE_SPEED
            self.sety(self.ycor() - y_increment)
            for p in self.paddle:
                p.sety(p.ycor() - y_increment)
