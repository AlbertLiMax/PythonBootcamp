from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        work_sec = LONG_BREAK_MIN
        reps = 0
        timer_label.config(text="Break",  bg=YELLOW, fg=RED, font=(FONT_NAME, 50, "bold"))
    elif reps % 2 == 0:
        work_sec = SHORT_BREAK_MIN
        timer_label.config(text="Break",  bg=YELLOW, fg=PINK, font=(FONT_NAME, 50, "bold"))
    else:
        work_sec = WORK_MIN
        timer_label.config(text="Work",  bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))

    count_down(60 * work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_mark += "✔"
        check_label.config(text=check_mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

start_button = Button(text="Start", highlightthickness=0, bg="white", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, bg="white", command=reset_timer)
reset_button.grid(column=2, row=2)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()