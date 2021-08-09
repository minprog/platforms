# Testing

Discovering bugs isn't easy, but it sure is easy to introduce bugs! Up to this point you've likely dabbled with manual testing to uncover any faults and bugs in your code. By quickly running your code with various inputs like so perhaps:

    $ python foo.py 4
    4
    $ python foo.py 5
    1
    $ python foo.py -1
    Sorry, can't handle negative numbers!

Makes sense right, because while you are working on a problem or assignment you are the expert right then and there. You'll know what the output should be and how the code should behave at that point. So quickly call your function, see what it does and if all looks good, well, submit it, done.

That is, until assignments grow a little. Maybe there's some teamwork involved. Maybe your code is part of a bigger program that is used for many years. That's where things start to get tricky. As more code is added, there's more room for bugs to hide and even more to test. Quickly it becomes impossible to test everything by hand.


### Automatic testing

Let's automate this. Now there are many things to test when it comes to software. Here's a quick overview:

* Does the program do what we want it to do? Testing for this is called functional testing.
* But we might also be interested in performance metrics or security concerns. Things that aren't directly tied to functionality. Unsurprisingly, this is called non-functional testing.

There exists several strategies to go about testing:

* We can test the system as a whole. Run the entire program, see if it does what it should do. This is called system testing. While useful, it is often difficult to test every part of the program this way.
* Zooming in, whatever you write is likely part of a bigger program, and well, it needs to fit into this bigger program. This is called integration testing.
* Finally, there's the code you write, the smaller functions and modules. Testing these individually is called unit testing.

For this module we'll narrow our scope to unit testing. Testing small individual units of a program. These could be functions, classes, modules, you name it. The goal of this type of testing is ensuring, or rather re-assuring, that each unit of the program functions as desired.


### Unit testing

Effectively unit testing does not need to be much more than writing a script that calls your unit of code, and checks that it does what it's expected to do. Let's get started with an example, `get_median()`. There's a list of things of which we need the median.


    def get_median(items: list[int]) -> int:
        size = len(items)
        middle = size // 2
        return items[middle]
    

Now we could write a seperate script to automatically test this for us. Let's say we create a file called `test_median.py`:

    from median import median
    
    items = [1,2,3,4,5]
    expected_median = 3
    assert get_median(items) == expected_median

There we go, one unit test. Running this file will either succeed silently or you'll find an `AssertionError`. But, there's probably more to test. Does this function work with various numbers of items? What about an empty list of items? We could append more assertions, but it does get unwieldy fast. Not only because if one assertion fails, everything stops running. But also because we are likely going to be writing the same code over and over for our tests.


### pytest

In comes `pytest`, one of many unittesting frameworks for Python, but arguably a popular and easy to use one. You do need to install it through `pip`:

    pip install pytest

Here's how it works. Every test file needs to start with the `test_` prefix, so `test_median.py` above will do just fine. Then, every test itself is a function also prefixed with `test_`. For instance, to pytest-ify our unit test above we can write:

    from median import get_median

    def test_median_5():
        items = [1,2,3,4,5]
        expected_median = 3
        assert get_median(items) == expected_median

Once saved in a file called `test_median.py`, you can simply run `pytest` like so:

    $ pytest
    ========================= test session start =========================
    platform linux -- Python 3.9.0, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    rootdir: /home/foo
    collected 1 item

    test_median.py .                                                                                                 [100%]

    ========================== 1 passed in 0.02s ==========================

