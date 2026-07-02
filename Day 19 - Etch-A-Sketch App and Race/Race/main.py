from turtle import Turtle, Screen
import random

# Create the turtle that will draw on the screen

# user_choice = input("Please choose a color: Red, Orange, Yellow, Green, Blue, Indigo, or Violet: ").lower()


red = Turtle()
red.shape('turtle')
red.color('red')
red.penup()
red.setpos(-300,75)
red.pendown()
orange = Turtle()
orange.shape('turtle')
orange.color('orange')
orange.penup()
orange.setpos(-300,50)
orange.pendown()
yellow = Turtle()
yellow.shape('turtle')
yellow.color('yellow')
yellow.penup()
yellow.setpos(-300,25)
yellow.pendown()
green = Turtle()
green.shape('turtle')
green.color('green')
green.penup()
green.setpos(-300,0)
green.pendown()
blue = Turtle()
blue.shape('turtle')
blue.color('blue')
blue.penup()
blue.setpos(-300,-25)
blue.pendown()
indigo = Turtle()
indigo.shape('turtle')
indigo.color('indigo')
indigo.penup()
indigo.setpos(-300,-50)
indigo.pendown()
violet = Turtle()
violet.shape('turtle')
violet.color('violet')
violet.penup()
violet.setpos(-300,-75)
violet.pendown()

while (
    red.xcor() < 300
    and orange.xcor() < 300
    and yellow.xcor() < 300
    and green.xcor() < 300
    and blue.xcor() < 300
    and indigo.xcor() < 300
    and violet.xcor() < 300
):
    red.forward(random.randint(0, 3))
    orange.forward(random.randint(0, 3))
    yellow.forward(random.randint(0, 3))
    green.forward(random.randint(0, 3))
    blue.forward(random.randint(0, 3))
    indigo.forward(random.randint(0, 3))
    violet.forward(random.randint(0, 3))

    






moves = random.randint(0,10)


# Create the turtle window
screen = Screen()










# Keep the window open until it is clicked
screen.exitonclick()