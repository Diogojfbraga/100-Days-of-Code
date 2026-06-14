from Calculator_ascii import calculator_ascii

# print(calculator_ascii)

calculator_is_off = False

def addition():
    print("addition")

def subtraction():
    print("subtraction")

def multiplication():
    print("multiplication")

def division():
    print("division")

def calculate():
    first_number = int(input("What is your first number: "))

    print("+\n-\n*\n/\n")
    operation = input("Pick an Operation: ")

    next_number = int(input("What is your next number: "))

    if operation == '+':
        addition()
    if operation == '-':
        subtraction()
    if operation == '*':
        multiplication
    if operation == '/':
        division()


while calculator_is_off is False:
    calculate()


