# Table tennis with words

We are creating a new app: [table tennis with words](https://youtu.be/Wu1kSXpVV8Y?t=2319). These are the rules:

The word spoken must begin with the last letter of the previous word. If you cannot think of a word within three seconds, or repeat a word, you are out.

As part of this new app, we need the function below:


    def guess(word: str, previous_words: list[str], time: float): -> bool
        # TODO
        pass


Implement the function above. This function should return False if any rule is broken, True otherwise. Raise a `ValueError` if the input is invalid.

Write Pytest unnittests to test the function `guess` in a file called `test_tennis.py`. Be sure to test:

* Normal operation: normal input yields expected output
* Edgecases, such as empty lists, one letter words, the number 0, etc.
* Handling of illegal input