from turtle import Turtle, Screen
import random

# Create the turtle that will draw on the screen

# Create the turtle window
screen = Screen()

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

y_positions = [75, 50, 25, 0, -25, -50, -75]

user_choice = screen.textinput(title="Make your bet", prompt="Please choose a color: Red, Orange, Yellow, Green, Blue, Indigo, or Violet: ").lower()


all_turtles = []

for turtle_index in range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y_positions[turtle_index])

    all_turtles.append(tim)
    
if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        
        if turtle.xcor() > 250:
            winner = turtle.pencolor()
            is_race_on = False
            if user_choice == winner:
                print(f"The {winner} turtle won. Your turtle won")
            else:
                print(f"The {winner} turtle won. Your turtle lost")

            break

        turtle.forward(random.randint(0, 3))


# Keep the window open until it is clicked
screen.exitonclick()