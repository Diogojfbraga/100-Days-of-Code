# Creates a list containing all letters of the alphabet
alphabet = list("abcdefghijklmnopqrstuvwxyz")

# Controls whether the program should keep running
keep_running = True

# Gets the user's choices and returns them to the main program
def start():
    # Asks whether the user wants to encode or decode
    direction = input("Type 'encode' to encrypt , type 'decode to decryp:\n").lower()

    # Gets the message from the user
    text = input("Type your message:\n").lower()

    # Gets the shift amount from the user and converts it to an integer
    shift = int(input("Type the shift number:\n"))

    # Returns the user's inputs so they can be used outside the function
    return direction, text, shift


# Encrypts the original text using the shift amount
def encrypt(original_text, shift_amount):
    # Creates an empty string to store the encrypted message
    encrypted_text = ""

    # Loops through each letter in the original text
    for letter in original_text:

        # Checks if the current character is in the alphabet
        if letter in alphabet:

            # Checks if shifting the letter goes past the end of the alphabet
            if (alphabet.index(letter) + shift_amount) > 25:
                encoded = alphabet[shift_amount - 1]

            # If it does not go past the end, shift normally
            else:
                encoded = alphabet[alphabet.index(letter) + shift_amount]

            # Adds the encoded letter to the encrypted message
            encrypted_text += encoded

    # Prints the final encrypted message
    print(encrypted_text)


# Decrypts the original text using the shift amount
def decrypt(original_text, shift_amount):
    # Creates an empty string to store the decrypted message
    decrypted_text = ""

    # Loops through each letter in the original text
    for letter in original_text:

        # Checks if the current character is in the alphabet
        if letter in alphabet:

            # Checks if shifting backwards goes before the start of the alphabet
            if (alphabet.index(letter) - shift_amount) < 0:
                dencoded = alphabet[26 - shift_amount]

            # If it does not go before the start, shift backwards normally
            else:
                dencoded = alphabet[alphabet.index(letter) - shift_amount]

            # Adds the decoded letter to the decrypted message
            decrypted_text += dencoded

    # Prints the final decrypted message
    print(decrypted_text)


# Keeps running the program until the user chooses to stop
while keep_running:
    # Calls start() and stores the returned values
    direction, text, shift = start()

    # Runs encryption if the user selected encode
    if direction == 'encode':
        encrypt(text, shift)

    # Runs decryption if the user selected decode
    elif direction == 'decode':
        decrypt(text, shift)

    # Handles invalid options
    else:
        print("Please select the right option")

    # Asks the user whether they want to use the program again
    again = input("Use again? 'Y' or 'N'").lower()

    # Stops the loop if the user chooses no
    if again == 'n':
        print("Bye")
        keep_running = False