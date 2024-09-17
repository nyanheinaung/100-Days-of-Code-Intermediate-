import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search():
    site_to_search = entry_website.get()
    if site_to_search:
        try:
            with open("data.json", "r") as password_data:
                data = json.load(password_data)
        except FileNotFoundError:
            messagebox.showinfo(title="Error!", message="No Data File!")
        else:
            if site_to_search in data:
                messagebox.showinfo(title="User Data", message=f"Website: {site_to_search}\n"
                                                               f"Email: {data[site_to_search]["email"]}\n"
                                                               f"Password: {data[site_to_search]["password"]}")
            else:
                messagebox.showinfo(title="No Data", message="No records for the specified website.")
    else:
        messagebox.showinfo(title="Error!", message="Please enter a website to search!")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letter_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, tkinter.END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    site = entry_website.get()
    mail = entry_email_username.get()
    password = entry_password.get()

    if len(site) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        # is_ok = messagebox.askokcancel(title="Website", message=f"These are the details entered: \n"
        #                                                         f"Email: {mail} \n"
        #                                                         f"Password: {password} \n"
        #                                                         f"Is it ok to save?")
        # if is_ok:
        #     data_to_write = f"{site} | {mail} | {password}\n"

        new_data = {
            site: {
                "email": mail,
                "password": password,
            }
        }

        try:
            with open("data.json", "r") as password_data:
                # Try to read the data first
                data = json.load(password_data)
        except FileNotFoundError:
            with open("data.json", "w") as password_data:
                # If no file prior, create it
                json.dump(new_data, password_data, indent=4)
        else:
            # Update with the new entry if there is original data
            data.update(new_data)
            with open("data.json", "w") as password_data:
                # Then write to the file
                json.dump(data, password_data, indent=4)
        finally:
            # Do this no matter what
            entry_website.delete(0, tkinter.END)
            entry_password.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = tkinter.PhotoImage(file="logo.png")
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
label_website = tkinter.Label(text="Website:")
label_website.grid(column=0, row=1)

label_email_username = tkinter.Label(text="Email/Username:")
label_email_username.grid(column=0, row=2)

label_password = tkinter.Label(text="Password:")
label_password.grid(column=0, row=3)

# Entries
entry_website = tkinter.Entry(width=32)
entry_website.grid(column=1, row=1)
entry_website.focus()

entry_email_username = tkinter.Entry(width=51)
entry_email_username.grid(column=1, row=2, columnspan=2)
entry_email_username.insert(0, "testmail@gmail.com")

entry_password = tkinter.Entry(width=32)
entry_password.grid(column=1, row=3)

# Buttons
button_generate = tkinter.Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)

button_add = tkinter.Button(text="Add", command=save, width=43)
button_add.grid(column=1, row=4, columnspan=2)

button_search = tkinter.Button(text="Search", command=search, width=14)
button_search.grid(column=2, row=1)

window.mainloop()
