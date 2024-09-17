import tkinter
MILE_TO_KM = 1.609


def convert_distance():
    mile = 0
    try:
        mile = float(num_input.get())
    finally:
        km = mile * MILE_TO_KM
        text_output.config(text=f"{km:0.2f}")


window = tkinter.Tk()
window.minsize(width=300, height=150)
window.title("Mile to Km Converter")
window.config(padx=40, pady=40)

num_input = tkinter.Entry()
num_input.grid(column=1, row=0)
num_input.config(width=10)

text_miles = tkinter.Label(text="Miles")
text_miles.grid(column=2, row=0)
text_miles.config(padx=10)

text_km = tkinter.Label(text="Km")
text_km.grid(column=2, row=1)
text_km.config(padx=10)

text_other = tkinter.Label(text="is equal to")
text_other.grid(column=0, row=1)

text_output = tkinter.Label(text="0")
text_output.grid(column=1, row=1)

button = tkinter.Button(text="Calculate", command=convert_distance)
button.grid(column=1, row=2)

window.mainloop()
