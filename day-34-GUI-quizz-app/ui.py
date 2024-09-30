import tkinter as tk

FONT = ("Ariel", 20, "italic")
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text=f"Score: {0}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(height=250, width=300, bg="white")
        self.canvas.create_text((125,150), text="Question Text", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_img = tk.PhotoImage("images/true.png")

        false_img = tk.PhotoImage("images/false.png")


        self.window.mainloop()