from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = [choice(letters) for _ in range(nr_letters)]
    password_list += [choice(symbols) for _ in range(nr_symbols)]
    password_list += [choice(numbers) for _ in range(nr_numbers)]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, f"{password}")
    # Copy generated password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                        message=f"These are the detailes entered: \nEmail: {username} \n"
                                f"Password: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                data_entry = f"{website} | {username} | {password}\n"
                file.write(data_entry)
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(width=300, height=300, padx=30, pady=30, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 94, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", bg="white")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

website_entry = Entry(width=50)
website_entry.config(bg="white")
website_entry.focus()
website_entry.grid(sticky="w", column=1, row=1, columnspan=2)

username_entry = Entry(width=50)
username_entry.config(bg="white")
username_entry.grid(sticky="w", column=1, row=2, columnspan=2)
username_entry.insert(0, "matrix.ee91g@gmail.com")

password_entry = Entry(width=21)
password_entry.config(bg="white")
password_entry.grid(sticky="w"+"e", column=1, row=3)

generate_button = Button(command=generate_password)
generate_button.config(text="Generate Password", bg="white")
generate_button.grid(sticky="w"+"e",column=2, row=3)

add_button = Button(width=49, command=save)
add_button.config(text="Add", bg="white")
add_button.grid(sticky="w",column=1, row=4, columnspan=2)


window.mainloop()