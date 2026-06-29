import colorgram
import random
from turtle import Turtle, Screen, colormode

# Extract colours from image
colors = colorgram.extract("Day 18 - Hirst Painting/image.jpeg", 30)

colors_list = []

for color in colors:
    rgb = color.rgb
    colors_list.append((rgb.r, rgb.g, rgb.b))

# Remove unwanted background colours
for _ in range(4):
    colors_list.pop(0)

# Turtle setup
colormode(255)

tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Starting position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 10
dot_size = 15
spacing = 40

for row in range(number_of_dots):

    for _ in range(number_of_dots):
        tim.dot(dot_size, random.choice(colors_list))
        tim.forward(spacing)

    # Move to next row
    tim.left(90)
    tim.forward(spacing)
    tim.left(90)

    # Reverse direction for the next row
    tim.setheading(0 if row % 2 == 0 else 180)

screen = Screen()
screen.exitonclick()