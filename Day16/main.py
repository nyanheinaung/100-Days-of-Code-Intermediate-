# from turtle import Turtle, Screen
#
# johnson = Turtle()
# johnson.shape("turtle")
# johnson.color("aquamarine")
# johnson.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable
import random

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align["Pokemon Name"] = "l"
table.align["Type"] = "r"
print(table)

watch = random.randint(1,3)
if watch == 1:
    print("watch pretty woman")
elif watch == 2:
    print("watch godzilla")
else:
    print("watch transformer")


