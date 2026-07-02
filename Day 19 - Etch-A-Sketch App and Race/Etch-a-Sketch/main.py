from turtle import Turtle, Screen

# Create the turtle that will draw on the screen
tim = Turtle()

# Create the turtle window
screen = Screen()


# Move the turtle forward when W is pressed
def move_forward():
    tim.forward(10)


# Turn the turtle right when D is pressed
def move_right():
    tim.right(10)


# Turn the turtle left when A is pressed
def move_left():
    tim.left(10)


# Move the turtle backwards when S is pressed
def move_back():
    tim.backward(10)


# Clear everything drawn, then return the turtle to the middle
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# Start listening for keyboard input
screen.listen()

# Connect each key to a movement function
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="s", fun=move_back)
screen.onkeypress(key="c", fun=clear)

# Keep the window open until it is clicked
screen.exitonclick()