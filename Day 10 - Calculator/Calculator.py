# Imports the calculator ASCII art from another Python file
from Calculator_ascii import calculator_ascii


# Displays the calculator ASCII art
# print(calculator_ascii)


# Controls whether the calculator should stop running
# This variable is currently not being used
calculator_is_off = False


# Returns the result of adding two numbers
def addition(first_number, next_number):
    return first_number + next_number


# Returns the result of subtracting the second number from the first
def subtraction(first_number, next_number):
    return first_number - next_number


# Returns the result of multiplying two numbers
def multiplication(first_number, next_number):
    return first_number * next_number


# Returns the result of dividing the first number by the second
def division(first_number, next_number):
    return first_number / next_number


# Runs the calculator
# result defaults to None when starting a new calculation
def calculate(result=None):

    # Uses the previous result if the user wants to continue calculating
    if result is not None:
        first_number = result

    # Otherwise, asks the user for a new first number
    else:
        first_number = int(input("What is your first number: "))

    # Controls the calculation loop
    continue_calculating = True

    while continue_calculating:

        # Displays the available mathematical operations
        print("+\n-\n*\n/\n")

        # Asks the user to select an operation
        operation = input("Pick an Operation: ")

        # Asks the user for the next number
        next_number = int(input("What is your next number: "))

        # Performs addition
        if operation == "+":
            result = addition(first_number, next_number)

        # Performs subtraction
        elif operation == "-":
            result = subtraction(first_number, next_number)

        # Performs multiplication
        elif operation == "*":
            result = multiplication(first_number, next_number)

        # Performs division
        elif operation == "/":

            # Prevents division by zero
            if next_number == 0:
                print("You cannot divide by zero.")
                continue

            result = division(first_number, next_number)

        # Handles an invalid mathematical operation
        else:
            print("Invalid operation.")
            continue

        # Displays the complete calculation and result
        print(f"{first_number} {operation} {next_number} = {result}")

        # Asks the user what they want to do next
        next_operation = input(
            f"Type 'y' to continue calculating with {result}, "
            "'n' to start again, or 'off' to exit: "
        ).lower()

        # Continues calculating using the previous result
        if next_operation == "y":
            first_number = result

        # Stops the current loop and starts a new calculation
        elif next_operation == "n":
            continue_calculating = False
            calculate()

        # Stops the calculator
        elif next_operation == "off":
            continue_calculating = False

        # Handles an invalid choice
        else:
            print("Invalid choice.")
            continue_calculating = False


# Starts the calculator program
calculate()