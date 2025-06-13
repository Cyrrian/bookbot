from stats import count_words
from stats import count_chars

def get_book_text(book):
    
    with open(book) as b:
        book_contents = b.read()
    
    return book_contents

def main ():

    text = get_book_text("./books/frankenstein.txt")

    count_words(text)
    count_chars(text)

main()