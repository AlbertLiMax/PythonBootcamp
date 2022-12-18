import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_name = turtle.Turtle()
state_name.hideturtle()
state_name.penup()

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")

guessed_states = []

game_is_on = True
while game_is_on:
    if len(guessed_states):
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What's another state's name?").title()
    else:
        answer_state = screen.textinput(title="Guess the State",
                                        prompt="What's another state's name?").title()

    if answer_state == "Exit":
        game_is_on = False
        remain_state = []
        for state in data.state:
            if state not in guessed_states:
                remain_state.append(state)
        df = pandas.DataFrame(remain_state)
        df.to_csv("state_to_learn.csv", index=False)
        break

    if answer_state not in guessed_states and len(data[data.state == answer_state]):
        guessed_states.append(answer_state)
        x = int(data[data.state == answer_state].x)
        y = int(data[data.state == answer_state].y)
        state_name.goto(x, y)
        state_name.write(answer_state, align="center")

    if len(guessed_states) == 50:
        game_is_on = False