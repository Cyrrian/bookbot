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
    char_counts = {}
    
    for c in book:
        c = c.lower()

        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1

    return char_counts

#******************************
# Function: sort_char_counts
#******************************
def sort_char_counts(char_counts):
    sorted_list = []

    for char in char_counts:
        sorted_list.append({"char": char,"num": char_counts[char]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

def sort_on(dict):
    return dict["num"]