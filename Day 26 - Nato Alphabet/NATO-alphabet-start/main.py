from pathlib import Path
import pandas as pd

csv_path = Path(__file__).parent / "nato_phonetic_alphabet.csv"
data = pd.read_csv(csv_path)

# Create the NATO dictionary
phonetic_dict = {
    row.letter: row.code
    for index, row in data.iterrows()
}

print(phonetic_dict)

# Ask the user for a word
user_word = input("Please write a word: ").upper()

# Look up every letter in the dictionary
output = [
    phonetic_dict[letter]
    for letter in user_word
]

print(output)