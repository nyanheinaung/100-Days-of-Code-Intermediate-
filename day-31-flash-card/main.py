import pandas as pd
import random
import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 30, "italic")
WORD_FONT = ("Ariel", 40, "bold")
MAIN = "English"
TRANS = "Myanmar"
FLASH_TIME = 3000
WORD_COUNT = 10

#-----------------------------------------------------------------------------------------------#
# Read from CSV and concat two dataframes, reindex them and convert the result to a single CSV
#     df1 = pd.read_csv("Eng-Myanmar1.csv", encoding="utf-8")
#     df2 = pd.read_csv("Eng-Myanmar2.csv", encoding="utf-8")
#
#     pd.concat([df1, df2]).dropna().to_csv("Eng-Myanmar.csv", sep=",", encoding="utf-8", index=False)
#
# To Remove something from dataframe, just drop the index
# df.drop(x) <-x can be anything
#
#-----------------------------------------------------------------------------------------------#

df = pd.read_csv("Eng-Myanmar.csv")
word_list = df.to_dict()
right_index = []
wrong_index = []
current_words = []
index = -1
is_front = True

def add_word():
    random_index = random.randint(0, len(df)-1)
    if random_index not in current_words:
        current_words.append(random_index)
    else:
        add_word()

def create_current_session():
    for _ in range(WORD_COUNT):
        add_word()

def got_it_right():
    global index
    remaining = len(current_words)

    if remaining > 1 and index != -1:
        current_words.pop(index)
        flip_canvas()
    elif remaining == 1:
        current_words.pop(0)
        got_it_right()
    else:
        canvas.itemconfig(canvas_language, text="")
        canvas.itemconfig(canvas_word, text="Well Done!\nFinished today's Session")

def got_it_wrong():
    flip_canvas()

def wait_a_bit():
    window.after(FLASH_TIME, flip_canvas)

# Flip canvas
def flip_canvas():
    global index
    global is_front
    remaining = len(current_words)
    if remaining:
        if is_front:
            button_wrong.config(state=tk.DISABLED)
            button_right.config(state=tk.DISABLED)

            index = random.randint(0, remaining-1)
            canvas.itemconfig(canvas_image, image=img_card_front)

            main_word = df[MAIN][current_words[index]]

            canvas.itemconfig(canvas_language, text=MAIN)
            canvas.itemconfig(canvas_word, text=main_word)
            wait_a_bit()

        else:
            button_wrong.config(state=tk.NORMAL)
            button_right.config(state=tk.NORMAL)

            translation = df[TRANS][current_words[index]]

            canvas.itemconfig(canvas_language, text=TRANS)
            canvas.itemconfig(canvas_word, text=translation)

        is_front = not is_front

# Create UI
window = tk.Tk()
window.title("Flash Cards Learning")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

img_card_back = tk.PhotoImage(file="card_back.png")
img_card_front = tk.PhotoImage(file="card_front.png")

canvas = tk.Canvas(width=850, height=550, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=5, rowspan=5)

canvas_image = canvas.create_image(425, 275, image=img_card_front)
canvas_language = canvas.create_text(400, 150, text="Language", font=LANGUAGE_FONT, justify="center", )
canvas_word = canvas.create_text(400, 200, text="word", font=WORD_FONT, justify="center", width=700, anchor="n")

img_wrong = tk.PhotoImage(file="wrong.png")
button_wrong = tk.Button(image=img_wrong, command=got_it_wrong, borderwidth=0, highlightthickness=False)
button_wrong.grid(column=1, row=5)

img_right = tk.PhotoImage(file="right.png")
button_right = tk.Button(image=img_right, command=got_it_right, borderwidth=0, highlightthickness=False)
button_right.grid(column=3, row=5)

# Mode 1
create_current_session()
flip_canvas()

# Mode 2

# Mode 3

window.mainloop()
