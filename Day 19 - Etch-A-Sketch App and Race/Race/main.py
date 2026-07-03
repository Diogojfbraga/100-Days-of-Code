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
            print(turtle.color())
            # is_race_on = False
        turtle.forward(random.randint(0, 3))



# while (
    
        
#         turtle.xcor() < 10
#         or orange.xcor() < 10
#         or yellow.xcor() < 10
#         or green.xcor() < 10
#         or blue.xcor() < 10
#         or indigo.xcor() < 10
#         or violet.xcor() < 10
# ):
#     red.forward(random.randint(0, 3))
#     orange.forward(random.randint(0, 3))
#     yellow.forward(random.randint(0, 3))
#     green.forward(random.randint(0, 3))
#     blue.forward(random.randint(0, 3))
#     indigo.forward(random.randint(0, 3))
#     violet.forward(random.randint(0, 3))


# turtle_coord = []


# turtle_coord.append(('red',red.xcor()))
# turtle_coord.append(('orange',orange.xcor()))
# turtle_coord.append(('yellow',yellow.xcor()))
# turtle_coord.append(('green',green.xcor()))
# turtle_coord.append(('blue',blue.xcor()))
# turtle_coord.append(('indigo',indigo.xcor()))
# turtle_coord.append(('violet',violet.xcor()))

# print(turtle_coord)

# coord = 0
# winner = ""

# for turtle_name, turtle_x in turtle_coord:

#     if turtle_x > coord:
#         coord = turtle_x
#         winner = turtle_name
#         if user_choice == winner:
#             print("You won")
#         else:
#             print(f"{winner} Won, you lose!!")

        












# Keep the window open until it is clicked
screen.exitonclick()