from turtle import Turtle
import random

BALL_SPEED = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset_ball()
        self.bounce(random.randint(-45, 45), "wall")

    def move(self):
        self.forward(BALL_SPEED)

    def bounce(self, strike_angle, target):
        if target == "wall":
            new_heading = -strike_angle + random.randint(-2, 2)
        else:
            new_heading = 180 - strike_angle + random.randint(-2, 2)
        self.setheading((new_heading+360) % 360)

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce(random.randint(-5, 5) + self.heading(), "player")
