import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
FONT = ("Impact", 10, "normal")

# display the map
states_data = pd.read_csv("50_states.csv")

screen.addshape(image)
turtle.shape(image)
turtle.penup()
score = 0

# places the state name on the map.
state_placer = turtle.Turtle()
state_placer.penup()
state_placer.hideturtle()

# create a list of all the states.
states_list = states_data['state'].to_list()
# create a list of all the correct guesses.
correct_guesses = []
# missed states.
learn_list = []

game_is_on = True

# begin the game.
while game_is_on:
    answer_state = screen.textinput(title=f"({score}/50) Guess the State!",
                                    prompt="What's a State name (type 'exit' to quit)?: ").title()
    # if answer was correct.
    if answer_state in states_list:
        # if answer has already been guessed.
        if answer_state in correct_guesses:
            continue
        x_axis = states_data[states_data.state == answer_state].x.iloc[0]
        y_axis = states_data[states_data.state == answer_state].y.iloc[0]
        # place the state name on the map.
        state_placer.setx(int(x_axis))
        state_placer.sety(int(y_axis))
        state_placer.write(f"{answer_state.title()}", align="center", font=FONT)
        # increment correct answers.
        score += 1
        # add the correct guesses to the list.
        correct_guesses.append(answer_state)
        # check to see if all states have been guessed.
        if len(correct_guesses) == 50:
            # end the game.
            game_is_on = False
    # exit the game when done.
    if answer_state.lower() == 'exit':
        # create a list of missed states to learn.
        learn_list = [state for state in states_list if state not in correct_guesses]
        learn_df = pd.DataFrame(learn_list)
        states_to_learn = learn_df.to_csv("states_to_learn.csv")
        game_is_on = False
