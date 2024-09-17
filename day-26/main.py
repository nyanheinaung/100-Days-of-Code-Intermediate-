import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_code_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_coded_name():
    name = input("Please enter your name: ")
    try:
        nato_name = [nato_code_dict[char] for char in name.upper()]
    except KeyError:
        print("Sorry, names with alphabets only please.")
        generate_coded_name()
    else:
        print(f"Your coded name is: {nato_name}")

    # nato_name = [nato_code_dict[char] if char.isalpha() else char for char in name.upper()]


generate_coded_name()
