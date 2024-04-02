import turtle
import pandas as pd

SCREEN = turtle.Screen()
SCREEN.title("U.S. States Game")
# add an IMAGE as the turtle shape
IMAGE = "blank_states_img.gif"
SCREEN.addshape(IMAGE)
turtle.shape(IMAGE)

data = pd.read_csv("USA_states.csv")
all_states = data.state.to_list()
ATTEMPTS = 0
MAX_ATTEMPTS = 50
guessed_states = []

"""
TO-DO:
1. check if guess is among the 50 states.
2. write correct guesses onto the map.
3. use a loop to allow user to keep guessing.
4. record the correct guesses in a list.
5. keep track of the score.
"""
while ATTEMPTS < MAX_ATTEMPTS:
    # generate a pop-up user input window on the Screen
    answer_state = SCREEN.textinput(title=f"{ATTEMPTS}/50 states correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [
            item for item in all_states if item not in guessed_states]
        # convert data in a list into a pandas dataframe.
        missing_states_data = pd.DataFrame(
            missing_states, columns=["Index", "States"])
        # convert dataframe to a csv file.
        missing_states_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        ATTEMPTS += 1
        guessed_states.append(answer_state)
        # write turtle to x&y location of state.
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("black")
        # extract data for the row corresponding to the state the user input.
        state_data = data[data.state == answer_state]
        # guessed
        t.goto(int(state_data.x), int(state_data.y))
        # the item method returns the 1st item on a row.
        t.write(state_data.state.item())
        # alternatively we could have gone with: t.write(answer_state)

"""
turtle.mainloop() 
# this is used in lieu of the exitonclick. In this case, we do not need it because in the while
loop we have a condition that will exit the game already.
"""
