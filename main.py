import sys

from stats import get_word_count
from stats import get_char_counts
from stats import sort_char_counts

#******************************
# Function: load_book
#******************************
def load_book(file):
    
    with open(file) as f:
        book = f.read()
    
    return book

#******************************
# Function: print_report
#******************************
def print_report(file, word_count, char_counts):
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in char_counts:
        if  char["char"].isalpha():
            print (f"{char['char']}: {char['num']}")

    print("============= END ===============")

#******************************
# Function: main
#******************************
def main ():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file = sys.argv[1]

    book = load_book(file)

    words = get_word_count(book)
    chars = sort_char_counts(get_char_counts(book))

    print_report(file, words, chars)

    #print(f"{words} words found in the document")
    #print(chars)

main()