import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcom to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like\n"))


# Retrieves the characters according with the input
password = []

for letter in range(nr_letters):
    password.append(random.choice(letters))

for symbol in range(nr_symbols):
    password.append(random.choice(symbols))

for number in range(nr_numbers):
    password.append(random.choice(numbers))


# Randomises the characters
random_pass = []
final_password = ""

for shuffle in range(len(password)):
    random_pass.append(random.choice(password))

# Merges in to a word
for char in random_pass:
    final_password += char

print(f"Your password is: {final_password}")

   
