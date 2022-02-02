# Testing

Discovering bugs isn't easy, but it sure is easy to introduce bugs! Up to this point you've likely dabbled with manual testing to uncover any faults and bugs in your code. By quickly running your code with various inputs like so perhaps:

    $ python3 foo.py 4
    4
    $ python3 foo.py 5
    1
    $ python3 foo.py -1
    Sorry, can't handle negative numbers!

Makes sense right, because while you are working on a problem or assignment you are the expert right then and there. You'll know what the output should be and how the code should behave at that point. So quickly call your function, see what it does and if all looks good, well, submit it, done.

That is, until assignments grow a little. Maybe there's some teamwork involved. Maybe your code is part of a bigger program that is used for many years. That's where things start to get tricky. As more code is added, there's more room for bugs to hide and even more to test. Quickly it becomes impossible to test everything by hand.


### Automatic testing

Let's automate this. Now there are many things to test when it comes to software. Here's a quick overview:

* Does the program do what we want it to do? Testing for this is called functional testing.
* But we might also be interested in performance metrics or security concerns. Things that aren't directly tied to functionality. Unsurprisingly, this is called non-functional testing.

There exists several strategies to go about testing:

* We can test the system as a whole. In other words, run the entire program and see if it does what it should do. This is called system testing. While useful, it is often difficult to test every part of the program this way.
* Zooming in, whatever you write is likely part of a bigger program, and well, it needs to fit into this bigger program. This is called integration testing.
* Finally, there's the code you write, the smaller functions and modules. Testing these individually is called unit testing.

For this module we will narrow our scope to unit testing. Testing small individual units of a program. These could be functions, classes, modules, you name it. The goal of this type of testing is ensuring, or rather re-assuring, that each unit of the program functions as desired.


### Unit testing

Effectively unit testing does not need to be much more than writing a script that calls your unit of code, and checks that it does what it's expected to do. Let's get started with an example, `get_median()`. There's a list of things of which we need the median.


    def get_median(items: list[int]) -> int:
        size = len(items)
        middle = size // 2
        return items[middle]
    

Now we could write a seperate script to automatically test this for us. Let's say we create a file called `test_median.py`:

    from median import get_median
    
    items = [1,2,3,4,5]
    expected_median = 3
    assert get_median(items) == expected_median

There we go, one unit test. Running this file will either succeed silently or you'll find an `AssertionError`. But, there's probably more to test. Does this function work with various numbers of items? What about an empty list of items? We could append more assertions, but it does get unwieldy fast. Not only because if one assertion fails, everything stops running. But also because we are likely going to be writing the same code over and over for our tests.


## pytest

In comes `pytest`, one of many unittesting frameworks for Python, but arguably a popular and easy to use one. You do need to install it through `pip`:

    pip3 install pytest

Here's how it works. Every test file needs to start with the `test_` prefix, so `test_median.py` above will do just fine. Then, every test itself is a function also prefixed with `test_`. For instance, to pytest-ify our unit test above we can write:

    from median import get_median

    def test_odd_length():
        items = [1,2,3,4,5]
        expected_median = 3
        assert get_median(items) == expected_median

Once saved in a file called `test_median.py`, you can simply run `pytest` like so:

    $ pytest
    ========================= test session start =========================
    platform linux -- Python 3.9.0, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    rootdir: /home/foo
    collected 1 item

    test_median.py .                                                [100%]

    ========================== 1 passed in 0.02s =========================

A few things happened here. `pytest` went looking in the current directory for any test files, those starting with `test_`. Then ran each of those files looking for functions starting with `test_`. This process is generally called test discovery and different testing frameworks will have different ways of doing this. This is just how `pytest` does it.

Then, with our one test discovered, `pytest` will run the test. For convenience, `pytest` uses Python's built-in `assert` statements. Other frameworks might have their own assertion methods. So all `pytest` does here is run the function and if an assertion fails, the test fails and otherwise it succeeds. In this case 100%, all of 1 test succeeded!


### Exceptions

So far we have tended to treat exceptions as if they were errors and were something to avoid. But many modern programming languages including Python have ways of dealing with exceptions. As follows:

    text = input("give me a number")
    try:
        number = int(text)
    except ValueError:
        number = 0

Through `try` and `except` we can try to execute a snippet of code and if it happens to fail due to some exception (`ValueError` above) we can deal with the exception. This is a powerful feature as it's often easier to ask forgiveness than to get permission. For instance, in the example above it is difficult to imagine each case in which we can convert a string into an integer. The string might exist of only numbers, but a `.` is also allowed. But not more than one `.` though! Whereas the other way around, well we can just try to make it an integer and see what happens.

Exceptions and tests go hand in hand. As you'll find yourself thinking about edgecases and erroneous cases. For instance, what's the median of an empty list `[]`? Arguably that is undefined and an exception really. Probably best to `raise` an exception in this case. Let's adjust our implementation of `get_median` to the following:

    def get_median(items: list[int]) -> int:
        size = len(items)

        if size == 0:
            raise ValueError("Cannot get a median from an empty list.")

        middle = size // 2
        return items[middle]

Now we can test for this. Test whether the function raises a certain exception. Here's how you do it in `pytest`:

    import pytest
    from median import get_median

    def test_empty():
        with pytest.raises(ValueError):
            get_median([])

This test will pass if a `ValueError` is raised and fail if it did not.


## Fixtures

Earlier we tested `get_median` with an input namely `[1,2,3,4,5]`. Odds are that almost every test you'll write needs some input, or rather some constant or fixed things that we are going to test with. Or in testing terminology, fixtures.

`pytest` has a simple way of handling fixtures. You mark a function as a fixture and can then use it as input of tests. Here's what it looks like:


    import pytest
    from median import get_median

    @pytest.fixture()
    def odd5():
        return [1,2,3,4,5]

    def test_odd_length(odd5):
        expected_median = 3
        assert get_median(odd5) == expected_median


Note a couple things, a fixture is marked with the `@pytest.fixture()` decorator. If you haven't seen this `@` syntax before, not to worry. All you need to know is, this marks the function below as a fixture. Then note `test_odd_length` accepts a parameter with the exact same name as the fixture above. That's how `pytest` knows what to pass in to your test.

But hang on, this is more lines of code than what we had before. Why should we want this? Several reasons actually. Perhaps the obvious reason is re-use of fixtures. If we're writing multiple tests, we can now easily use `odd5` as input for those tests. In this case the input is simply a list of numbers, but you can imagine this could be a very complex datastructure of several objects too. Perhaps more interestingly for our usecase, fixtures can be parameterized. Here's what that looks like:


    import pytest
    from median import get_median

    @pytest.fixture(params=[1, 3, 5, 7])
    def odd(request):
        return list(range(1, request.param + 1))

    def test_odd_length(odd):
        expected_median = odd[len(odd) // 2]
        assert get_median(odd) == expected_median


Now we're not just testing for 5 items, but rather 4 different odd lengths. The syntax is a little weird, with `params=`, `request` as a parameter to `odd()` and `request.param` as a way to access the parameter. But that's what it is.

If we run pytest with this code in `test_median.py` we'll see:

    $ pytest
    ========================= test session start =========================
    platform linux -- Python 3.9.0, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    rootdir: /home/foo
    collected 4 items                                                     

    test_median.py ....                                             [100%]

    ========================== 4 passed in 0.02s =========================

Even though the file contains 1 test function, 4 tests are run. One for each version of the fixture. In fact, any test function taking the fixture `odd` will now be called 4 times. This is a very quick way to test for many different inputs, without needing to write a lot of code!
