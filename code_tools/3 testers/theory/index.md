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

