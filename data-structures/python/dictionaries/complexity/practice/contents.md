# Practice with time complexity of dictionaries
> **You don't have to hand in these practice exercises.** They're here for you to test yourself. Did you fully understood the theory you just learned?
>
> If there is an exercise that you don't know how to make, review the theory again. If that doesn't help, discuss the exercise with another student and/or the teacher.

**Exercise 1**
Measure the dictionaries and list in a similar way as in the video, but now focus on the `in` operator. Use runs with lists and dictionaries of different sizes. Use 10, 100, 1000, and 10,000 (ad maybe 100,000 if you have a fast computer). For every run, execute the `in`-operation 100,000 times (to get reliable results). Write down the results (you can do this manually), and create a table with the runtimes that looks something like this:

	size  |  list |  dict
	10    |  0.14 |  0.09
	100   | ??.?? | ??.??
	1000  | ??.?? | ??.??
	10000 | ??.?? | ??.??

You can use the code below to get started

	from time import time
	from random import randint

    # create a list or dictionary containing n items

	# test speed
	iterations = 100000
	start = time()
	for _ in range(iterations):

		# TODO: enter code to test

	end = time()
	print(f'The time elapsed: {end-start:.2f} seconds (with {iterations} iterations)')
