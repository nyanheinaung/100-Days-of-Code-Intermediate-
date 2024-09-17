import turtle

import colorgram
import random
from turtle import Turtle, Screen
from color_list import extract_color


colorList = extract_color("hirst-painting.jpg")

turtle.colormode(255)
tom = Turtle()
tom.penup()
tom.hideturtle()
tom.speed(0)
tom.setposition(-350, -350)

for i in range(10):
    for j in range(10):
        tom.dot(20, random.choice(colorList))
        tom.forward(70)
    tom.setposition(-350, -280+i*70)

sc = Screen()
sc.exitonclick()