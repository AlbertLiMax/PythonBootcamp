from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=600)
window.config(padx=20, pady=20)

#Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button

def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

#Entry

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

window.mainloop()