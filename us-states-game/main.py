import turtle
import pandas

FONT = ("Ariel", 10, "normal")
FINISH_FONT = ("Ariel", 20, "bold")

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(740, 510)

name_writer = turtle.Turtle()
name_writer.penup()
name_writer.hideturtle()
name_writer.goto(0, 0)

states_info = pandas.read_csv("50_states.csv")
all_states = states_info.state.to_list()

correct_answers = []

while len(correct_answers) < 50:

    if correct_answers:
        answer_state = screen.textinput(title=f"Correct Answers: {len(correct_answers)}/50",
                                        prompt="What's another state?")
    else:
        answer_state = screen.textinput(title="Guess the state", prompt="Enter the state name below")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in all_states and answer_state not in correct_answers:
        state_location = states_info[states_info.state == answer_state]
        name_writer.goto(state_location.x.item(), state_location.y.item())
        name_writer.write(answer_state, align="center", font=FONT)
        name_writer.goto(0, 0)
        correct_answers.append(answer_state)

if len(correct_answers) == 50:
    name_writer.goto(0, 0)
    name_writer.write("Well done. You have correctly guessed all the states!", align="center", font=FINISH_FONT)
else:
    missing_states = [state for state in all_states if state not in correct_answers]
    # for state in all_states:
    #     if state not in correct_answers:
    #         missing_states.append(state)
    pandas.DataFrame(missing_states).to_csv("Missing state names.csv")


# Customization code!!
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
