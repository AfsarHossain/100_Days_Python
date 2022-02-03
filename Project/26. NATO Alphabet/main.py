import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
# print(data.to_dict())

# TODO 1: Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# TODO 2: Create a list of the phonetic code words from a word that the user inputs.
# word = input("Enter a word: ").upper()

# print(word)
# TODO: output_list = [new_item for item in list]

# TODO: ---------------------------------------------------------
# TODO: Mine Solution
# check = True
#
# while check:
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#         check = False
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#
# print(output_list)
# TODO: ----------------------------------------------------------


def generate_phonetic():

    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
