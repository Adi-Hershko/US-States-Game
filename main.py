import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def print_state(coor, state):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(coor)
    new_turtle.write(state, align="center")


file = pandas.read_csv("50_states.csv") # ALL
answer_state = screen.textinput(title="Guess The State", prompt="What's another state's name?").title()
state_list = file["state"].to_list()
correct_guesses = []
while len(correct_guesses) < 50:
    if answer_state == "Exit":
        break

    state_info = file[file.state == answer_state]
    if not state_info.empty and answer_state not in correct_guesses:
        location = (int(state_info["x"]), int(state_info["y"]))
        print_state(location, state_info.state.item())
        correct_guesses.append(answer_state)
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Guess The State", prompt="What's another state's name?").title()

missed_states = []
for state in state_list:
    if state not in correct_guesses:
        missed_states.append(state)

missed_guesses = {
    "Guesses missed": missed_states
}

data = pandas.DataFrame(missed_guesses)
data.to_csv("Missed Guesses.csv")
