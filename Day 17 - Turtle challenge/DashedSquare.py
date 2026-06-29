from turtle import Turtle, Screen, colormode

tim = Turtle()

tim.shape('turtle')
tim.color("red", "green")

colormode(255)

# Dashed Square
for _ in range(4):
    for _ in range (15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()
    tim.right(90)

screen = Screen()
screen.exitonclick()