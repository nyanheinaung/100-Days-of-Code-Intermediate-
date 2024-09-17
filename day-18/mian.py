import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
# tim.shape("turtle")
turtle.colormode(255)
tim.speed(0)

# colors = ["red", "orange", "blue", "cyan", "yellow", "green", "brown", "purple", "pink", "violet", "black", "gold", "silver"]

# def draw_polygon(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for n_sides in range(3, 11):
#     tim.color((random.random(), random.random(), random.random()))
#     draw_polygon(n_sides)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
#
#
# tim.pensize(15)
# for _ in range(500):
#     tim.color(random_color())
#     tim.forward(random.randint(20, 50))
#     if random.random() < 0.5:
#         tim.right(90)
#     else:
#         tim.left(90)


def draw_spirograph(circle_count):
    for i in range(circle_count):
        tim.color(random_color())
        tim.setheading(tim.heading() + 360/circle_count)
        tim.circle(100)


draw_spirograph(20)





screen = Screen()
screen.exitonclick()