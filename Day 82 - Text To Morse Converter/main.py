import re

## Get message from user and convert into upper case
user_string = input("Please type a word or Morse code: ").upper()


## Morse Dictionary
morse_alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/"
}


## Store the translated characters
final_output = []


## Check if user entered Morse code
if user_string.startswith((".", "-")):

    ## No spaces needed between translated letters
    separator = ""

    ## Reverse dictionary to translate Morse into letters
    reverse_morse = {value: key for key, value in morse_alphabet.items()}

    ## Convert Morse into letters
    ## One space separates letters, two or more spaces separate words
    for symbol in re.sub(r" {2,}", " / ", user_string).split():
        if symbol in reverse_morse:
            final_output.append(reverse_morse[symbol])
        else:
            print(f"Character '{symbol}' is not supported.")

else:

    ## Add a space between each Morse character
    separator = " "

    ## Convert each letter into Morse code
    for letter in user_string:
        if letter in morse_alphabet:
            final_output.append(morse_alphabet[letter])
        else:
            print(f"Character '{letter}' is not supported.")


## Join the list and print the final result
print(f"Translated text: {separator.join(final_output)}")