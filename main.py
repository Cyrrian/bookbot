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
# Function: main
#******************************
def main ():

    book = load_book("./books/frankenstein.txt")

    words = get_word_count(book)
    chars = sort_char_counts(get_char_counts(book))

    print(f"{words} words found in the document")
    print(chars)

main()