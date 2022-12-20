from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=100)
window.config(padx=20, pady=20)

label_1 = Label(text="Miles", justify=CENTER, font=("Arial", 12))
label_1.grid(column=2, row=0)
label_1.config(pady=10)

label_2 = Label(text="Km", justify=CENTER, font=("Arial", 12))
label_2.grid(column=2, row=1)

label_3 = Label(text="0", justify=CENTER, font=("Arial", 12))
label_3.grid(column=1, row=1)
label_3.config(padx=30, pady=10)

label_4 = Label(text="is equal to", font=("Arial", 12))
label_4.grid(column=0, row=1)
label_4.config(padx=20)

def miles_to_km():
    miles = float(entry.get())
    km = round(miles * 1.609)
    label_3.config(text=f"{km}")

button = Button(text="Calculate", justify=CENTER,
                font=("Arial", 12, "bold"), command=miles_to_km)
button.grid(column=1, row=2)

entry = Entry(width=10, justify=CENTER)
entry.insert(END, string="0")
entry.grid(column=1, row=0)
entry.focus()

window.mainloop()