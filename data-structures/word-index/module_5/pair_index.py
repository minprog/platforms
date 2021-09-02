import sys, string

###############
# Old functions
###############

def read_stopwords():
    # Your previous solution goes here
    pass

def filter_word(word, stopwords):
    # Your previous solution goes here
    pass

def show_search_results(line_numbers):
    # Your previous solution goes here
    pass


###############
# Assignment 3
###############

def build_pair_index(filename, stopwords, recency_size=5):
    # Assignment 3A
    pass

def search_pair_index(word_1, word_2, book_index):
    # Assignment 3A
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
        started = False

        # Read the lines in the file and give them a number
        for i, line in enumerate(f.readlines()):
            if line[:9] == "*** START":
                started = True
            elif line[:7] == "*** END":
                # Stop reading
                break

            elif started:
                # i starts at 0, while our line numbers should start at 1
                line_number = i+1

                # Split the line into a list of strings (splits on spaces)
                for s in line.split():
                    word = convert_word(s)

                    # Filter empty strings and stop words
                    if len(word) > 0 and not filter_word(word, stopwords):
                        processed_words.append((word, line_number))

    return processed_words

def user_input_pair_search(book_index):
    """
    User input loop. For every line provided as input, extract words, convert
    them, find the line numbers, and show results.
    """
    while True:
        line = input()
        words = [convert_word(s) for s in line.split()]
        line_numbers = search_pair_index(words[0], words[1], book_index)
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
    book_index = build_pair_index(sys.argv[1], stopwords)

    print("Index built for", sys.argv[1]+".",
          "Type the word you want to look up.")

    # Start the user input loop
    user_input_pair_search(book_index)
