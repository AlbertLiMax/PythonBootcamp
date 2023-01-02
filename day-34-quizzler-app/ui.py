from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=400, height=400, padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.quiz_text = self.canvas.create_text(150, 125, text="Quiz", width=280,
                                                 fill="black", font=("Ariel", 14, "bold"))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.score_text = Label(text="Score: 0", bg=THEME_COLOR, fg="white",
                                justify=CENTER, font=("Ariel", 12))
        self.score_text.grid(column=1, row=0)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.get_next_question()

        self.true_button = Button(width=100, height=97, highlightthickness=0,
                                  image=true_image, command=self.select_true)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(width=100, height=97, highlightthickness=0,
                                   image=false_image, command=self.select_false)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def update_score(self, is_correct):
        self.window.after(1000, self.get_next_question)
        self.score_text.config(text=f"Score: {self.quiz.score}")
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

    def select_true(self):
        is_correct = self.quiz.check_answer("True")
        self.update_score(is_correct)

    def select_false(self):
        is_correct = self.quiz.check_answer("False")
        self.update_score(is_correct)
