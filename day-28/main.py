import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECONDS_IN_MIN = 60
reps = 0
timer = None
started = False

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    operation_name.config(text="Timer")
    check_mark.config(text="")
    global started
    started = False

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global started
    if not started:
        started = True
        global reps
        reps += 1

        work_sec = WORK_MIN * SECONDS_IN_MIN
        short_break_sec = SHORT_BREAK_MIN * SECONDS_IN_MIN
        long_break_sec = LONG_BREAK_MIN * SECONDS_IN_MIN

        if reps % 2 != 0:
            countdown(work_sec)
            operation_name.config(text="WORK", fg=GREEN)
        elif reps % 8 == 0:
            countdown(long_break_sec)
            operation_name.config(text="BREAK", fg=RED)
        else:
            countdown(short_break_sec)
            operation_name.config(text="BREAK", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = count//60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        global reps
        mark = ""
        work_sessions = reps//2
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

operation_name = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
operation_name.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", command=start_timer, font=(FONT_NAME, 20))
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", command=reset_timer, font=(FONT_NAME, 20))
reset_button.grid(column=2, row=2)

check_mark = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_mark.grid(column=1, row=3)

window.mainloop()
