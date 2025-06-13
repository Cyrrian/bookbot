def count_words(book):
    words = book.split()
    num_words = len(words)

    print(f"{num_words} words found in the document")

def count_chars(book):
    char_counts  = {}
    
    for c in book:
        c = c.lower()

        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1

    print(char_counts)