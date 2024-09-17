from turtle import Turtle, Screen
import random

# tim = Turtle()
screen = Screen()


# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def move_clockwise():
#     tim.setheading(tim.heading()-10)
#
#
# def move_counter_clockwise():
#     tim.setheading(tim.heading()+10)
#
#
# def clear_drawing():
#     tim.penup()
#     tim.home()
#     tim.clear()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(fun=move_forward, key="w")
# screen.onkey(fun=move_backward, key="s")
# screen.onkey(fun=move_counter_clockwise, key="a")
# screen.onkey(fun=move_clockwise, key="d")
# screen.onkey(fun=clear_drawing, key="c")


screen.setup(500, 400)

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
count = len(colors)
turtles = []
for i in range(count):
    newTurtle = Turtle(shape="turtle")
    newTurtle.color(colors[i])
    newTurtle.penup()
    newTurtle.goto(x=-230, y=-120+i*40)
    turtles.append(newTurtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(f"You bet {user_bet}.")

winner_decided = False
game_over = False
winner = ""

while not game_over:
    count = 0
    for turtle in turtles:
        if turtle.xcor() >= 230 and not winner_decided:
            winner = turtle.pencolor()
            winner_decided = True
        elif turtle.xcor() < 230:
            turtle.forward(random.randint(3, 10))
        else:
            count += 1
    if count == 7:
        game_over = True


print(f"The winner is Mr.{winner}.")

if user_bet == winner:
    print("Congratulations. You won the bet.")
else:
    print("Too bad! You lose.")


screen.exitonclick()
