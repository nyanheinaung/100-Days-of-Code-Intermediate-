from turtle import Turtle

PLAYER_SPEED = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.color("red")
        self.shape("turtle")
        self.penup()
        self.reset_position()

    def move(self):
        self.forward(PLAYER_SPEED)

    def reset_position(self):
        self.goto(0, -280)
