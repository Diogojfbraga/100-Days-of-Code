# Create the snake body


from turtle import Turtle, Screen
import time, random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('Black')
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]

squares = []

scoreboard = Turtle()





for position in starting_positions:
    new_square = Turtle(shape='square')
    new_square.penup()

    new_square.color('gray', 'white')
    new_square.goto(position)
    squares.append(new_square)



food_location = []

def food():

    new_food = Turtle(shape="circle")
    new_food.penup()
    new_food.color("green")
    new_food.shapesize(stretch_len=0.5, stretch_wid=0.5)


     # Detect collision with food
    food_x = random.randint(-300,300)
    food_y = random.randint(-300,300)

    new_food.goto(food_x, food_y)

    return new_food

current_food = food()

# Move the snake
game_is_on = True

# Turn the turtle right when D is pressed
def move_right():
    squares[0].right(90)


# Turn the turtle left when A is pressed
def move_left():
    squares[0].left(90)

score = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)


    for square_number in range(len(squares) -1, 0, -1):
        new_x = squares[square_number - 1].xcor()
        new_y = squares[square_number - 1].ycor()
        squares[square_number].goto(new_x, new_y)

    squares[0].forward(10)

        # Control the snake
    screen.listen()  
    screen.onkeypress(key="d", fun=move_right)
    screen.onkeypress(key="a", fun=move_left)
    
    
    if squares[0].distance(current_food) < 10:
        scoreboard.clear()
        score += 1

        current_food.hideturtle()
        current_food = food()

        
        
    scoreboard.color("white")
    scoreboard.penup()
    scoreboard.goto(0,250)
    scoreboard.write(f"Score: {score}", move=False, align="center", font=("Arial", 18, "normal"))
    scoreboard.hideturtle()     

    




    # print(squares[0].xcor())
    # print(food_x)
    # print(squares[0].distance(food_x, food_y))   


    


screen.listen()
# screen.onkey(key="a", fun=move_left)



# Create a scoreboard
# Detect collision with wall
# Detect colision with tail


screen.exitonclick()