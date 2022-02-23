# Many submissions of cash

We asked students to implement the following function:


    def number_of_coins(change: int, coins: list[int]) -> int:
        """
        Given an amount of change in cents, and a list of coins in cents,
            calculate how many coins are needed to fulfill the change.
        Raises a TypeError in case floats are given instead of integers.
        Raises a ValueError in case of negative values, or coins of value 0.
        """


For example:


    print(number_of_coins(41, [25, 10, 5, 1])) # prints 4



To further restrict the assignment we added:

* You may assume that a greedy strategy (exchanging as many as possible of the largest exchangable coin first) will always yield the correct answer.
* You may assume that the user will never enter any other values than integers and floats.
* You may assume that the user will always enter a `list` of integers or floats for coins.
* In case the change cannot be met exactly, give as much as possible, without exceeding the total. For instance if there are only quarters (25) as coins and the change is 97, give 3 quarters,

At the end of the day, thirteen students submitted their work. You can find each implementation in the `submissions` folder. That however leaves us with the following challenge: grading. Which of these thirteen submissions are incorrect and why?


### What to do

[Download the distribution code](testing_cash.zip).

Write unittests in Pytest to test this assignment. Mark each assignment as correct or incorrect below. In case the assignment is incorrect, write down why. Submit all your unittests in a file named `test_cash.py` on the bottom of this page. 


### A bit of help

Hold on, before you jump right in, we have added some scaffolding to get you going. You will find two additional files:

1. `conftest.py`, long story short, this file contains some pytest specific code that adds a command line option to pytest (`--path`) and uses these paths to load in the student implementations of `number_of_coins`. These implementations are passed to any unittest requesting a `number_of_coins` fixture. Through this file you will able to write tests like so:


        def test_something(number_of_coins):
            assert number_of_coins(41, [25, 10, 5, 1]) == 4


    And call them like so:

        pytest --path submissions/1/cash.py
        pytest --path submissions/1/cash.py --path submissions/2/cash.py

2. Thirteen programs is a lot to test, and it is easy to get overwhelmed by the number of tests. `run_tests.py` is here to help. This script will run pytest for each submission in the `submissions` folder and dump the output of the test to `outputs/1.txt` (for each submission respectively). Just run it like so:

    
        $ python3 run_tests.py
        Testing - submissions/1/cash.py => outputs/1.txt   | SUCCESS
        Testing - submissions/2/cash.py => outputs/2.txt   | FAILED
        Testing - submissions/3/cash.py => outputs/3.txt   | SUCCESS
        ...
        
    
    Handy right!


### Some piece of mind

* You may assume all implementations are deterministic, there is no randomness in any implementation.
* You may assume infinite loops do not exist.
* You may assume the student code does not contain anything malicious.
* We believe only **one** submission is correct, but feel free to prove us wrong!


### Submission 1
    
<input type="radio" name="form[correct1]" value="correct" required>
<label for="correct1">correct</label>
<input type="radio" name="form[correct1]" value="incorrect" required>
<label for="correct1">incorrect</label><br/>
<textarea name="form[explanation1]" rows="4" required> </textarea>

### Submission 2
    
<input type="radio" name="form[correct2]" value="correct" required>
<label for="correct2">correct</label>
<input type="radio" name="form[correct2]" value="incorrect" required>
<label for="correct2">incorrect</label><br/>
<textarea name="form[explanation2]" rows="4" required> </textarea>

### Submission 3
    
<input type="radio" name="form[correct3]" value="correct" required>
<label for="correct3">correct</label>
<input type="radio" name="form[correct3]" value="incorrect" required>
<label for="correct3">incorrect</label><br/>
<textarea name="form[explanation3]" rows="4" required> </textarea>

### Submission 4
    
<input type="radio" name="form[correct4]" value="correct" required>
<label for="correct4">correct</label>
<input type="radio" name="form[correct4]" value="incorrect" required>
<label for="correct4">incorrect</label><br/>
<textarea name="form[explanation4]" rows="4" required> </textarea>

### Submission 5
    
<input type="radio" name="form[correct5]" value="correct" required>
<label for="correct5">correct</label>
<input type="radio" name="form[correct5]" value="incorrect" required>
<label for="correct5">incorrect</label><br/>
<textarea name="form[explanation5]" rows="4" required> </textarea>

### Submission 6
    
<input type="radio" name="form[correct6]" value="correct" required>
<label for="correct6">correct</label>
<input type="radio" name="form[correct6]" value="incorrect" required>
<label for="correct6">incorrect</label><br/>
<textarea name="form[explanation6]" rows="4" required> </textarea>

### Submission 7
    
<input type="radio" name="form[correct7]" value="correct" required>
<label for="correct7">correct</label>
<input type="radio" name="form[correct7]" value="incorrect" required>
<label for="correct7">incorrect</label><br/>
<textarea name="form[explanation7]" rows="4" required> </textarea>

### Submission 8
    
<input type="radio" name="form[correct8]" value="correct" required>
<label for="correct8">correct</label>
<input type="radio" name="form[correct8]" value="incorrect" required>
<label for="correct8">incorrect</label><br/>
<textarea name="form[explanation8]" rows="4" required> </textarea>

### Submission 9
    
<input type="radio" name="form[correct9]" value="correct" required>
<label for="correct9">correct</label>
<input type="radio" name="form[correct9]" value="incorrect" required>
<label for="correct9">incorrect</label><br/>
<textarea name="form[explanation9]" rows="4" required> </textarea>

### Submission 10
    
<input type="radio" name="form[correct10]" value="correct" required>
<label for="correct10">correct</label>
<input type="radio" name="form[correct10]" value="incorrect" required>
<label for="correct10">incorrect</label><br/>
<textarea name="form[explanation10]" rows="4" required> </textarea>

### Submission 11
    
<input type="radio" name="form[correct11]" value="correct" required>
<label for="correct11">correct</label>
<input type="radio" name="form[correct11]" value="incorrect" required>
<label for="correct11">incorrect</label><br/>
<textarea name="form[explanation11]" rows="4" required> </textarea>

### Submission 12
    
<input type="radio" name="form[correct12]" value="correct" required>
<label for="correct12">correct</label>
<input type="radio" name="form[correct12]" value="incorrect" required>
<label for="correct12">incorrect</label><br/>
<textarea name="form[explanation12]" rows="4" required> </textarea>

### Submission 13
    
<input type="radio" name="form[correct13]" value="correct" required>
<label for="correct13">correct</label>
<input type="radio" name="form[correct13]" value="incorrect" required>
<label for="correct13">incorrect</label><br/>
<textarea name="form[explanation13]" rows="4" required> </textarea>
