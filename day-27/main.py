import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Ariel", 23, "bold"))
# my_label.pack()
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=30)

my_label["text"] = "New Text!"

# Button
def button_click():
    # print("Clicked!")
    # my_label["text"] = "Button Clicked!"
    value = num_input.get()
    my_label.config(text=value)

button = tkinter.Button(text="Click Me", command=button_click)
# button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button", command=button_click)
new_button.grid(column=2, row=0)

# Entry
num_input = tkinter.Entry(width=10)
# num_input.pack()
num_input.grid(column=3, row=2)



window.mainloop()
