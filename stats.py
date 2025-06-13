# Description: This module contains functions to calculate statistics from a text file.

# This function reads a text file and counts the number of words in it.
def get_num_words(book):
    with open(book) as f:
        file_contents = f.read()
    num_words = len(file_contents.split())
    return f'Found {num_words} total words'

# This function takes text from a file as a string and returns the number of times each character, (including symbols and spaces), appears in the string.
def get_char_count(book):
    with open(book) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        char_list = []
        for char in file_contents:
            found = False
            for item in char_list:
                if item['char'] == char:
                    item['num'] += 1
                    found = True
                    break
            if not found:
                char_list.append({'char': char, 'num': 1})
        return char_list

# This function is used to sort the character count dictionary by the number of occurrences of each character.
def sort_on(dict):
    return dict["num"]
