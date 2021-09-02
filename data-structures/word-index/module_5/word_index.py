import sys, string

##############
# Assignment 1
##############

def read_stopwords():
    with open("stopwords.txt") as f:
        stopwords = [s.strip() for s in f.readlines()]
        # Assignment 1A
        pass

def filter_word(word, stopwords):
    # Assignment 1B
    pass


##############
# Assignment 2
##############

def build_index(filename, stopwords):
    # Assignment 2A
    pass

def search_index(word, book_index):
    # Assignment 2B
    pass

def show_search_results(line_numbers):
    # Assignment 2C
    pass


###############
# Starting code
###############

def convert_word(s):
    """
    Strips a word from all puncuation, whitespace, and digits. Then converts
    the word into all lower case.
    """
    return s.strip(string.punctuation + string.whitespace + \
                   string.digits).lower()

def read_gutenberg_file(filename, stopwords):
    """
    Reads `filename` and returns a list of tuples.

    The list of tuples consists of words and the linenumber that that specific
    word was found on. Each word is first stripped from punctuation, whitespace,
    and digits, and is also converted to lower case and checked to not be in the
    list of `stopwords`.

    NOTE: Understanding this code is not essential to completing this exercise
    """
    processed_words = []

    with open(filename, encoding='utf8') as f:

        # Read the first line of the file
        line = f.readline()

        # Our line numbers should start at 1
        line_number = 1

        # Find the start of the book, ignore all lines before
        while line[:9] != "*** START":
            line = f.readline()
            line_number += 1

        # Keep reading until we find the end of the book
        while line[:7] != "*** END":
            line = f.readline()
            line_number += 1

            # Split the line into a list of strings (splits on spaces)
            for substring in line.split():
                word = convert_word(substring)

                # Filter empty strings and stop words
                if len(word) > 0 and not filter_word(word, stopwords):
                    processed_words.append((word, line_number))

    return processed_words

def user_input_search(book_index):
    """
    User input loop. For every line provided as input, convert it, find the line
    numbers, and show results.
    """
    while True:
        line = input()

        searched_word = convert_word(line)
        line_numbers = search_index(searched_word, book_index)
        show_search_results(line_numbers)

if __name__ == "__main__":
    # Read the stopwords from the stopwords file
    stopwords = read_stopwords()

    # If there is no argument provided
    if len(sys.argv) == 1:
        print("No arguments provided.",
              "Please specifiy the file you want to search.")

        # Stop the program
        sys.exit()

    # Uses first command line argument as input file to build an index of words
    book_index = build_index(sys.argv[1], stopwords)

    print("Index built for", sys.argv[1]+".",
          "Type the word you want to look up.")

    # Start the user input loop
    user_input_search(book_index)
