class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def StillHasQuiz(self):
        return self.question_number < len(self.question_list)


    def NextQuiz(self):
        question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {question.text} (True/False)?: ").title()
        self.question_number += 1
        self.CheckAnswer(user_answer, question.answer)


    def CheckAnswer(self, u_answer, q_answer):
        if u_answer == q_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {q_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")