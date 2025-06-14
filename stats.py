#******************************
# Function: get_word_count
#******************************
def get_word_count(book):
    words = book.split()
    num_words = len(words)

    return num_words

#******************************
# Function: get_char_counts
#******************************
def get_char_counts(book):
    char_counts  = {}
    
    for c in book:
        c = c.lower()

        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1

    return char_counts