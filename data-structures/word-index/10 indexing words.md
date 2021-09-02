# Indexing words

For this assignment you will build an indexing system for books from
[Project Gutenberg](http://www.gutenberg.org/). There are several
formats available for each book, but easiest to process will definitely be
*Plain Text*. Two books are already included in plain text format as part of
the assignment, but feel free to download some other books and use those to
test your system with instead.

Download the assignment files [here](module_5.zip). Unzip the module into your
working directory.

Open one of the downloaded books and take a look at the format. Note that these
books do not contain any page numbers, but are just line after line filled with
text from the book. If you would want to refer to a specific word in this book,
then the simplest way would be to just refer to the line number where that word
occurs.

This is exactly the type of index you will have to construct: We want to be
able to quickly search if a word occurs in a book and if so, at what lines.
Quite a bit of starting code has already been provided in `word_index.py`.
Most importantly, the function `read_gutenberg_file()` will take the filename
of a book and read its contents, and handling the user input has also already
been taken care of. The rest of the book indexing system is up to you to write.

## Filtering words

The provided `read_gutenberg_file()` function is almost complete. It skips the
licensing part of the file, splits the entire file into words, removes
punctuation and converts all the words to lowercase. However, some words are so
common, you might want to actually skip indexing them entirely. These most
common words are generally called *stop words* when processing text. A short
list of stop words has also already been provided in `stopwords.txt`.

Your first assignment is to complete the part of the program that filters these
stop words. Start by thinking what operations you will need to perform in order
to filter all words in the book: For each word you will need to check if it is
in the collection of stop words. Since this checking is repeated many times,
making that operation more efficient would definitely effect the speed of your
program.

Consider what representation would be most efficient for this type of search.
Open the `word_index.py` file and finish the function `read_stopwords()`, which
currently contains the stopwords in a list. Transform the list to a
representation of your choice, if needed, and *return* that representation.

Next up is the `filter_words()` function, which takes two arguments: `word`,
which is the word being checked and `stopwords`, which is your own
representation of the collection of stopwords. This function should return
`True` if the word should be filtered (i.e. it needs to be removed) or `False`
if it should **not** be filtered. If the word is equal to the empty string `''`
or if the word occurs in the stop words, it should be filtered.

### Goal

Filter very common word words from the book to prevent adding them to the
index. Complete the functions `read_stopwords()` and `filter_word()` to do
this.

### Question 1

Consider the total number of stop words passed to `filter_word()` to be the
the functions input size **N**.

What is the complexity of your `filter_word()` function? Explain your answer.

## Indexing words

With these two functions completed, the `read_gutenberg_file()` function should
now work correctly. It will return you a list of tuples, where each tuple
contains a word and its line number. So, looping over the result of
`read_gutenberg_file()` will give you pairs of words and their line numbers,
which you can then use to build your book index.

This indexing program will be an interactive look-up, meaning you will not know
beforehand how many and which words will be searched in our book. The function
should therefore return an index of all the words which can be easily searched.
When a word is looked up, the program should return all the line numbers where
this word occurs. The function `build_index()` in `word_index.py` should return
this book index structure, on which you can later perform the searches.

Think about a kind of data structure would an efficient choice to build this
book index with. Complete the `build_index()` function and have it return your
indexing data structure. Use the `read_gutenberg_file()` to loop through the
file and add each word and line number to your indexing structure.
`read_gutenberg_file()` takes two arguments `filename`, which is the file you
want to read and `stopwords`, which is your stopwords structure that will be
used to filter the words in the book.

Next step is to search this book index, which is done with the `search_index()`
function. The function takes 2 arguments; `word`, which is the word being
searched, and `book_index`, which is your constructed index for the book. This
function should return the line numbers where the word occurs in the book.

The function that handles user input has already been provided, so the user can
type words in the terminal when the program is run, which are then looked up
using your `search_index()` function. The last step is to show the results of
the search back to the user. This should be done with the function
`show_search_results()`, which takes the line numbers returned by your search
as an argument. Use the `print` function and some nice formatting to show the
the user at which line numbers the word can be found in the book.

### Goal

Build a searchable index for a book and allow the user to search that book
using input. Complete the functions `build_index()`, `search_index()` and
`show_search_results()` to do this.

### Testing your program

Now it is time to test your indexing and searching functions! Run the program
by typing

```
python word_index.py darwin_origin_of_species.txt
```

This command will run your `build_index()` function and then allow you to
provide input on the command line. Type a word, followed by an *\<enter\>*, to
see where it occurs in *On the Origin of Species*. You can quit your program
any time by pressing *\<ctrl-c\>*.

Some of the most famous observations Darwin wrote about in this book are on the
different species of birds that occurred on the Galapagos islands and their
relative diversity between each island. So search for the word *"birds"* and
see if the correct line numbers are returned. Verify the first couple of line
numbers and check that the word *"birds"* indeed occurs there in the book.

A topic Darwin didn't write about at all in *On the Origin of Species* was
dinosaurs. Search for the word *"dinosaurs"* in the book and see if indeed
correctly nothing is returned. Note that the program should **not** crash or
produce an error if you search for words that do not occur in the book.

Lastly, lets test that the word filtering also works correctly. A word that
definitely occurs in the book, but should be filtered out by the stop words
list would be *"the"*. Search for this word and check that indeed nothing is
returned.

Test any other words you want to search and maybe try a different book too.
Remember you can quit the program any time by pressing *\<ctrl-c\>*. Make sure
you are convinced all parts work correctly and understand how the program works
as a whole before moving on to the next part.

### Question 2

Consider the total number of words from the book included in the index to be
the input size **N** for the `search_index()` function.

What is the complexity of using your `search_index()` function to search for a
single word in the index? Explain your answer.

Take a look at the `user_input_search()` function provided in the starting code
and check where it uses your `search_index()` function. This function loops
through all the words searched by the user. Consider the total number of words
that is searched in `user_input_search()` to be that functions input size
**M**.

What is the complexity of the `user_input_search()` function in terms of **N**
and **M**? Explain your answer.
