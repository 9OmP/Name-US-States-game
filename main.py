import pandas as pd
import turtle

df = pd.read_csv("50_states.csv")
l1 = df.state.to_list()
x = df.x.to_list()
y = df.y.to_list()
guessed_states = []

game_is_on = True
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
turtle.shape(image)


def draw_state(answer_state, x, y):
    print(x, y)
    writer.goto(x, y)
    writer.write(answer_state, False, align='left', font=('arial', 8, 'bold'))


while len(set(guessed_states)) < 50:
    answer_state = turtle.textinput(title=f"Guess the State {len(set(guessed_states))}/50 States Correct",
                                    prompt="What's the state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        break
    if answer_state in l1:
        print(f"{answer_state} is a Valid State")
        guessed_states.append(answer_state)
        index = l1.index(answer_state)
        draw_state(answer_state, x[index], y[index])

not_in_list = [x for x in l1 if x not in guessed_states]
print(not_in_list)
new_data = pd.DataFrame(not_in_list)
new_data.to_csv("states to learn.csv")


screen.exitonclick()
