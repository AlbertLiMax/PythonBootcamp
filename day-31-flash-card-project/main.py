from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(width=1000, height=650, padx=50, pady=50, bg=BACKGROUND_COLOR)

# ---------------------------- DATABASE SETUP ----------------------- #
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")

french_dict = df.to_dict(orient="records")

current_word = {}
timer = None
def next_card():
    global timer, current_word
    try:
        window.after_cancel(timer)
    except ValueError:
        pass
    # Pick a random french word
    current_word = choice(french_dict)
    flash_card.itemconfig(display_image, image=front_image)
    flash_card.itemconfig(title_text, text="French", fill="black")
    flash_card.itemconfig(word_text, text=current_word["French"], fill="black")
    timer = window.after(3000, flip_card)

def flip_card():
    window.after_cancel(timer)
    flash_card.itemconfig(display_image, image=back_image)
    flash_card.itemconfig(title_text, text="English", fill="white")
    flash_card.itemconfig(word_text, text=current_word["English"], fill="white")

def is_known():
    french_dict.remove(current_word)
    df = pandas.DataFrame(french_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- IMAGES ------------------------------- #
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# ---------------------------- UI SETUP ----------------------------- #
flash_card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
display_image = flash_card.create_image(400, 263, image=front_image)

title_text = flash_card.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
word_text = flash_card.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
next_card()
flash_card.grid(column=0, row=0, columnspan=2)

right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)


window.mainloop()

