# BookBot: A simple book analysis tool

# Importing necessary modules
import sys
from stats import get_num_words, get_char_count, sort_on

sys.argv

if len(sys.argv) > 1:
    book = sys.argv[1] 
    print(sys.argv[1])
else:
    sys.exit("Usage: python3 main.py <path_to_book>")


# This function reads a book file and prints its contents.
def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return f"{file_contents}"

# This function is the main entry point of the program.
def main():
    d = get_char_count(book)
    # Sort the character count dictionary by the number of occurrences of each character
    d.sort(reverse=True, key=sort_on)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book}...')
    print('----------- Word Count ----------')
    print(get_num_words(book))
    print('--------- Character Count -------')
    # Print the character counts, excluding non-alphabetic characters
    for d_i in d:
        if d_i['char'].isalpha():
            print(f'{d_i["char"]}: {d_i["num"]}')  
    print('============= END ===============')
main()

# using sys.argv to get the book path from command line arguments
 