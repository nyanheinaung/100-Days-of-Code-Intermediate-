from turtle import Turtle
import random

COLORS = ("violet", "indigo", "blue", "green", "yellow", "orange", "red")
MIN_SPEED = 10
MAX_SPEED = 20


class Car(Turtle):
    def __init__(self, direction, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 3)
        self.color(COLORS[random.randint(0, 6)])
        self.speed = random.randint(MIN_SPEED, MAX_SPEED)
        self.direction = direction
        self.setposition(position)
        self.going = True

    def remove_car(self):
        self.hideturtle()

    def move(self):
        if self.going:
            self.forward(self.speed*self.direction)
