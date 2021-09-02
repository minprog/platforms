
## Assignment 3: Near word pairs

For this last assignment you will extend the indexing program from the previous
assignment, so it can support a more interesting type of search. You should
keep working with the same text files as before, but now you should work on the
`pair_index.py` file.

Looking for individual words can already tell you quite a lot about where to
find certain information, but a pair of words would of course allow the user to
be a lot more specific about what exactly they are looking for. The 2 words
they are looking for might not necessarily be *directly* next to each other,
but you would expect them to *near* enough, if they are indeed related. So,
what you will build is a search for *word pairs*: Do these two words occur
close together anywhere in the book?

Let's say for now that "near enough" is within 5 words. This means building
an index where we can search for a pair of words and find all lines where these
two words occur within 5 words of each other. Stopwords should again be
excluded from indexing and also excluded from adding distance between words.
The line number added for a pair should always be the higher line number of the
two, independent of the order in which the words appeared.

### Example

Lets take a look at a specific example. Below are 6 lines from *On the Origin of
Species*, with the original line number added at the start of each line. We'll
look specifically at the pair of words *"varieties"* and *"species"* for this
small bit of sample text.

    13671: varieties[V1]. These are strange relations on the view of each species[S1]              
    13672: having been independently created, but are intelligible if all species[S2]          
    13673: first existed as varieties[V2].                                                     
    13674:                                                                                 
    13675: As each species[S3] tends by its geometrical ratio of reproduction to    

The word varieties occurs twice, marked by `[V_]`, and the word species occurs
3 times, marked by `[S_]`. Running the indexing of the pairs on this text
would result in 3 matches within 5 words of each other:

* V1 and S1, distance 5 words, matched at line 13671
* S2 and V2, distance 4 words, matched at line 13673
* V2 and S3, distance 2 words, matched at line 13675

A couple of things to note here. First, it doesn't matter if the words are on
the same line like `V1` and `S1`, on seperate lines like `S2` and `V2`, or even
in separate paragraphs like `V2` and `S3`. Only the distance between the
matched words counts. Secondly, it might seem like the distance between words
is too small, but remember that stopwords are ignored in the distance too.
*"These"*, *"are"*, *"on"*, *"the"*, *"of"* and *"each"* are all stopwords, so
the effective distance between `V1` and `S1` is only 5 words. Lastly, the same
word can be a part of multiple matches, like here `V2` matches with both `S2`
and `S3`.

If for this example the distance of recency would be increased to 10, then `V1`
and `S2` would also produce a match at line 13672 and `S1` and `V2` would
produce a second match at 13673. Increasing it even further, even V1 and S3
could produce another match at 13675. So what words are considered *near*
depends on how we set this distance parameter. Looking at this example, a
distance of 5 seems to produce reasonable results, so we'll use that as the
default. Searching an index built on this part of the text for the
words *"varieties"* and *"species"* should therefore give exactly 3 matches:
13671, 13673 and 13675.

### Building the index

This pair indexing system will become a separate Python program. A starting
template similar to `word_index.py` has been provided in `pair_index.py`. Some
of the functionality of the pair indexing program will be exactly the same as
for the single word index. These functions are listed under the section *Old
functions* and they can be copied from your `word_index.py` solution verbatim.
Start by adding your solution for these 3 functions to the file.

Next up is writing the function `build_pair_index()`, which should return an
index similar to your old `build_index()` function, but searchable by word
pairs, where a word pair is a tuple: `(word_1, word_2)`. Building
an indexing system in which you can search for word pairs can be a little
tricky, so we will guide you through the steps.

Eventually, your function should return a list of line numbers for every pair of
words that is in the text with a `recency_size` maximum number of words in
between. Let's say that we are currently looking at a word in the middle of the
text, which we will call `current_word`, and that `recency_size=5`, which means
that we will need take into account any potential word pair for this word that
has occurred within the last five words. This means that there should actually
be five pairs added to the index for every word processed.

Before we can add these new pairs to our big collection of pairs, we would need to know
what the five most recent words are. A good method of tracking these words as we
go is by creating a secondary list `recent_words` that is updated as we go. When
you index a new word, you can append it to that recent word list and remove the
least recent word at at the front of the list (which is now no longer *recent*).
This might look something like:

    recent_words.append(current_word)
    if len(recent_words) > recency_size:
        recent_words.pop(0)

Essentially, we are making a queue of words that holds a maximum of
`recency_size` words. The function `.pop(0)` removes the element at position `0`
(i.e. the front) from the list. The `if` statement allows the list of recent
words to fill up as the program is reading the first couple of words in the
book. Once the recent words list is full, you'll want to remove the least recent
element from the front of the list.

Start your function by copying your `build_index()` function. It should already
use the `read_gutenberg_file()` which converts and filters the words from the
`filename`-file. Use the code above to integrate a list of `recent_words`, and
test it before continuing. At this point your code should read words from a file
as a list of tuples, get a `current_word` from this list, add the word to your
index, at the end of a loop add it to a list of `recent_words`, and finally
after the main loop return the index. It is essential that your `current_word`
is not added to the `recent_words` list before adding the word to the index.

Now, instead of just adding the word to the index, we should add each possible
word pair to the index. Remove your code adding just one word to the index, and
replace it by a for-loop that goes over each of the entries in `recent_words`.
When the index is done, it should be possible to find each combination of the
recent words and the current words in the index, so the next step would be
adding each of these pairs separately to the index.

The program should add each of these pairs of the `current_word` and each of the
`recent_words` to the index. This means that, using default values, there should
be five pairs added to the index for every word processed. (Note that this is
not true for the first five words, as there are not five most recent words.)
Write the code that will add all these recent pairs of words to your index.
Store each pair of words together in the index in a such way that you can easily
search for that same pair of words again. Remember, the line number you add for
each pair should always be the line number of the  `current_word`.

Something to note while building your index is that order of these words in the
pair will most likely matter when trying to find that pair back. Your program
should however return a line number for each match, independent of the order
the words of a match occur in. You can fix this after implementing adding the
pairs to your index. The easiest solution would be to add *two* pairs, in the
two different orders, but that would double the number of pairs in the index.
Another solution might be to *sort* the two words alphabetically and then ensure
you always search for them in that same alphabetical order. You may implement
either solution for this.

Finally, the `search_pair_index()` function will need to be completed. The input
will be handled similarly as for `search_index()`, except that the user should
now type 2 words as input, separated by space. These 2 words are then passed to
`search_pair_index()`, together with the index you constructed. Search for
these two words to your pairs index, applying that same alphabetical sorting to
the word order here too, if you did so in the previous step. The function
should return the matching line numbers for each search. Use the same format
for this as you did in `word_index.py`, so your old `show_search_results()`
will work correctly here too.

### Goal

Construct an indexing program to search for pairs of words that occur within 5
words of each other in a book. Complete the functions `read_stopwords()`,
`filter_words()`, `show_search_results()`, `build_pair_index()` and
`show_search_results()` in the file `pair_index.py` to do this.

### Testing

Test you program by running

```python
pair_index.py darwin_origin_of_species.txt
```

This will build the word pairs index using a recency size of 5. Try some pairs
of words and check that they occur together in the document.For example, the
words *"blue"* and *"bird"* both occur plenty of times in *On the Origin of
Species*, but occur only **once** close together. Use the program and check
that these words indeed occur close together in the book at the position you
found.

Additionally, confirm that the ordering of the words does not matter when
searching. Start by searching for *"Darwin, Charles"*, which should still
produce two results, even if the name never occurs in that order. Make sure
your program is handling these case correctly too.

Lastly, compare the program to the example given before. Search for the words
*"species"* and *"varieties"*, which should give many matches in the book.
Starting from line 13670, there should be exactly 3 matches; 13671, 13673 and
13675, corresponding the matches from the 6 example lines shown earlier.

If it is difficult to find these or other occurences specifically, you may want
to create a file that only has this piece of text, or your own version of a
piece of text, such that you can test it in isolation. Remember to include
`*** START` and `*** END` in these files, or the program will not start reading!

### Question 3

Is the complexity of your `search_pair_index()` function the same or
different from your `search_index()` from assignment 2? Why or why not? Explain
your answer.

Is the complexity of your `build_pair_index()` function the same or
different from your `build_index()` from assignment 2? Why or why not? Explain
your answer.

## Bonus Assignment

This assignment is completely optional, but can provide a nice challenge if you
are up for that. For this bonus assignment, you will need to make word pair
indices for two different books and see what word pairs overlap between these
books. Then you should find the top 10 pairs that occur the *most* between the
two books. So the end result of running the program sould be showing the top
10 most common overlapping word pairs between both the books.

Make a new python file called `common_word_pairs.py` and start by
copying in all the code from `pair_index.py`, as almost all of that code will
be relevant for this new program. The program should take **two** books as
arguments and build the word pair indices for both. You will need to modify
some parts of the starting code to do this. Testing your program should be done
by

```
python common_word_pairs.py darwin_origin_of_species.txt james_joyce_ulysses.txt
```

Next add your own functions to check which word pairs overlap between the two
indices. Then for these word pairs that do overlap, find the pairs that occur
most between the two books. Show the top 10 of the most common overlapping
pairs to user.

The steps here will involve some more difficult operations, but try and still
think about how to solve each of these *efficiently*. Specifically, finding the
overlapping pairs between the books and finding which of these pairs are the
most common between the books should be done efficiently.
