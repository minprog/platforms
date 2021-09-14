# Jaccard

For this assignment you will compare the similarity between two texts. Is *Dracula* of Bram Stoker, more similar to the work of Shakespeare or to the script of *La La Land*?

We will already provide you with some code that can compute the similarities between texts, based on the [Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index). The problem is, this code is not very efficient. Your goal is to improve it.

## Jaccard index

The Jaccard index is a metric to determine the similarity between two texts. Say we have two texts:

- Text 1: "A cat is not a caterpillar."
- Text 2: "My cat is a cat."

To compute the Jaccard index, we first have to determine the collection of all the *unique* words in the two texts. We call such a collection of unique words a **bag of words**.

- Bag of words for text 1 is: *a, cat, is, not, caterpillar*
- Bag of words for text 2 is: *my, cat, is, a*

Note that the bags of words contain no duplicate words.

To compute the Jaccard index, we divide the size of the *intersection* of both bags of words, by the size of their *union*.

- The intersection of both bags of words is: {*a, cat, is*}, containing 3 elements.
- The union of both bags of words is: {*my, a, cat, is, not, caterpillar*}, containing 6 elements.
- So, the Jaccard index is $$3/6=0.5$$

Mathematically you write this:

$$
J(A,B) = \frac{|A \cap B|}{|A \cup B|}
$$

Where $$A$$ and $$B$$ are the bags of words.

## Assignment

We've written some code that computes the Jaccard index of two text files. You can download the code here: [jaccard.zip](jaccard.zip)
You can run the code like this:

    $ python jaccard.py texts/cat.txt texts/cat2.txt
    Jaccard index of texts/cat.txt and texts/cat2.txt: 0.500

Unfortunately, the code is not particularly well written. It is very slow, and overly complicated. The files in the example above are very small, so in this case the code still runs quite fast. But if you try some other examples, you'll see the problem. This one takes much more time:

    $ python jaccard.py texts/her.txt texts/grimm.txt

And with this one it becomes unusably slow:

    $ python jaccard.py texts/holmes.txt texts/shakespeare.txt

It is up to you to improve this code.

Note: The text files contained in the download are copied from [Harvard's CS50 course](https://cs50.harvard.edu/x/2021/psets/5/speller/)

### Step 1: Analyze

First analyze the file. Read the file and try to understand how it is working. For every function in the file, write down (in the commentary above the function) its current big O complexity. How does the size of the input file affect the run time?

### Step 2: Improve

By making clever use of existing Python data structures, you can both make the code more elegant (simpler and easier to read) and much, much more efficient.

It should be possible to make this run very fast (in under a second):

    $ python jaccard.py texts/holmes.txt texts/shakespeare.txt

### Step 3: Analyze (again)

Again, for every function in the file, write in the commentary its new big O complexity. Write it down so that it's easy to see both the original complexity and the improved one.
