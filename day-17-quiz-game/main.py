from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# formating question bank
question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_bank)
# asking the questions
while quiz.StillHasQuiz():
    quiz.NextQuiz()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

