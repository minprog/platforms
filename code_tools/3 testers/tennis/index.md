# Table tennis with words

We are creating a new app: [table tennis with words](https://youtu.be/Wu1kSXpVV8Y?t=2319). These are the rules:

The word spoken must begin with the last letter of the previous word. If you cannot think of a word within three seconds, or repeat a word, you are out.

As part of this new app, we need the function below:

    def guess(word: str, previous_words: list[str], time: float) -> bool:
        # TODO
        pass

## Step 1, implement the function `guess`

Implement the function above. This function should return False if any rule is broken, True otherwise. Raise a `ValueError` if the input is invalid.

> Note that you don't have to implement the whole game! Just the function `guess` as described above.

## Step 2, test your implementation and improve if necessary

This assignment is all about thoroughly testing one function `guess`. While doing so you might find bugs or cases you hadn't thought of while implementing the function. It is up to you to not only write the tests, but also improve the code in case you stumble upon any bugs.

Write Pytest unnittests to test the function `guess` in a file called `test_tennis.py`. Be sure to test:

- Normal operation: normal input yields expected output
- Edgecases, such as empty lists, one letter words, the number 0, etc.
- Handling of any illegal input

> Important: You may assume that arguments to the function `guess` are always of the correct type. `word` will always be a string, `previous_words` will always be a list of strings and `time` a float. So there is no need to test for this.

Be thorough, rack your brains as to what you could and should test with this particular function. What input can you give it, and what should the output be? As a ballpark figure, you should find yourself writing about ten tests.
