import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
print(nato_data.head())
print(nato_data.to_dict())

letter2code = {
    row.tolist()[0]: row.tolist()[1]
    for (index, row) in nato_data.iterrows()
}

print(letter2code)

user_word = input("What is the name?\n")

print(
    [letter2code[i.upper()] for i in user_word]
)