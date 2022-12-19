import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")

#1. Create a dictionary in this format:
alphabet = {row.letter:row.code for (index, row) in df.iterrows()}

#2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
code = [alphabet[letter] for letter in word]

print(code)