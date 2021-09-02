
# Efficiency

For this assignment we are going to start with some short examples and
questions about **efficient** code. You probably have noticed by now that there
can be quite a few different ways to solve some problems in *Python*. Swapping
a `for` loop with a `while` loop should result in functionally the same code, but in
most cases the choice for one approach over another will have a measurable effect
on the code. Which approach you end up choosing, can depend on a few different factors:

1. Some approaches might have fewer lines of code to write than others (not always the
   best reason).
2. Some approaches might be more readable, requiring less documentation for the code to be
   understandable.
3. Some approaches might take less time computing when solving the same
   problem, making them faster to compute the same solution.

Note that all 3 of these are distinctly different criteria, and shorter code
definitely does not imply faster to compute. If it isn't code length, then what
*does* determine a program's speed?

## Measuring efficiency

A general rule for efficiency is that it becomes more important as the data you
are working with gets larger. If you have to process millions of data points,
then inefficient code might have you waiting for the results for a long time,
or worse, make your solution infeasible altogether. In science, we often
work with large data sets, so studying the fundamentals of efficient code for any
size of input will prove to be a useful tool.

In computer science, efficiency is usually expressed by the relationship
between the computation time of a piece of code and the size of its input. If
there is more data for a piece of code to process, then logically the
computation will take longer, but how much longer exactly determines how
efficient the code is. Let's take the simple function below as an example

	def sum_list(inputs):
		total = 0
		for elem in inputs:
			total += elem
		return total

As the number of elements in this list grows, so does the number of steps
in this for loop. So, we would naturally expect longer lists to take longer to
compute. Let's test that hypothesis by seeing how long different calls of this
function end up taking. We'll do this using the `time` library, which we can use
to measure the current time directly before and after the function. Below is a
general function, which will apply some function to a list and measure how long
this takes.

Next, we'll use the `random` library to generate an integer between *0* and *100*
and repeat this *N* times, to have a list of *N* random integers. You do not
have to understand the details of these functions, but they are used for all
tests and are, thus, shown here for completeness.

	import time
	import random

	def timed_function_list(function, input_list):
		# Measure start time
		start = time.time()
		# Call the function with the provided arguments
		result = function(input_list)
		# Measure end time
		end = time.time()

		print("The %s of %s elements took %6f seconds to compute." %
			  (function.__name__, str(len(input_list)).rjust(10), end-start))

		return result

	def random_list(N, max_int=100):
		# Generate N random numbers between 0 and max_int
		return [random.randint(0, max_int) for i in range(N)]

Now we have all the components to measure the `sum_list()` function. We can generate random inputs of size *N* using `random_list()` and use `timed_function_list()` to measure how long it takes to process each input.

The code below uses different powers of 10 as increasingly larger inputs (`**` is the power operator in *Python*). For each input size it generates a random list and times how long it took to compute the total using `sum_list()`.

	for i in range(5, 9):
		inputs = random_list(10**i)
		total = timed_function_list(sum_list, inputs)
		print("The sum total was", total)

	The sum_list of     100000 elements took 0.008087 seconds to compute.
	The sum total was 4951878
	The sum_list of    1000000 elements took 0.080046 seconds to compute.
	The sum total was 49488344
	The sum_list of   10000000 elements took 0.743973 seconds to compute.
	The sum total was 494901280
	The sum_list of  100000000 elements took 7.268038 seconds to compute.
	The sum total was 4949616780

Although not exactly, we can see that for each factor of 10 by which the length of the input list increases,
the result approximately requires 10 times longer to compute. Intuitively, this
might make sense, as the number of steps in the for loop grows linearly with
each element added to the list. This means the `sum_list()` function has a
linear increasing efficiency.

Quantifying this increase in efficiency is done more formally in computer
science using the big $$O$$ notation. The big $$O$$ is written
as a function of the input size *N*, so a simple linear increase would be
denoted as $$O(N)$$. As the size of the input *N* increases, so does
the computation time by a factor $$O(N)$$.

### Timing tests and the big O notation

The big $$O$$ notation is quite a coarse measure, which only
concerns what the biggest factor will be for the computation time as the
input grows. In contrast, these timing tests are accurate to the microsecond
($$10^{-6}$$ seconds), so there will always be some differences between the
theoretical factor and the measured scale factor. In addition, your computer
will also be performing other tasks in the background, so there will even be
differences in the times if you repeat the measurements, even though the
computation steps are identical every time. The measured results will therefore
not line up exactly with the predicted factors, but the effects should be big
enough to see the general trends.

*Note: Both these effects will be more pronounced for smaller input sizes, and
should smooth out as the input becomes larger, but computing for larger inputs
requires waiting for the results longer. For each of the experiments in this
assignment we've tried to strike a balance between the two, so the scale is
large enough to see the general trend for different input sizes, but does not
take too long to compute. Note that some of these experiments are therefore done
at different input scales, based on the complexity of the problems, so keep this
in mind when comparing the results between experiments.*

## Quadratic Complexity

So, the `sum_list` function has a complexity of $$O(N)$$, but
unfortunately, not all problems can be solved with a linear complexity. Let's
take a look at another example, where we are trying to count how often each
number occurs in our list. We will take a somewhat naive approach and generate
a new list indicating how often each number occurs:

	def count_occurrence(inputs):
		counts = []
		for elem_1 in inputs:
			# Counts for each element start at 0
			c = 0
			for elem_2 in inputs:
				# If the elements match, increase the count by 1
				if elem_1 == elem_2:
					c += 1

			# After comparing to all the elements in the list, add the count
			counts.append(c)

		# Return the list of counts for each element
		return counts

	for i in range(2, 5):
		inputs = random_list(10**i)
		counts = timed_function_list(count_occurrence, inputs)

		# Show the counts for the first 5 numbers
		for j in range(5):
			print("The number", inputs[j], "occurs", counts[j], "times")

	The count_occurrence of        100 elements took 0.000695 seconds to compute.
	The number 1 occurs 2 times
	The number 39 occurs 2 times
	The number 87 occurs 4 times
	The number 23 occurs 1 times
	The number 66 occurs 3 times
	The count_occurrence of       1000 elements took 0.042067 seconds to compute.
	The number 2 occurs 8 times
	The number 40 occurs 10 times
	The number 34 occurs 15 times
	The number 59 occurs 13 times
	The number 86 occurs 8 times
	The count_occurrence of      10000 elements took 4.298409 seconds to compute.
	The number 10 occurs 113 times
	The number 54 occurs 109 times
	The number 54 occurs 109 times
	The number 9 occurs 84 times
	The number 22 occurs 112 times

There are some important things to note here. Firstly, the number of elements we are
using to make this comparison is **much** smaller, in order to keep the
computation times manageable. Secondly, for this function, the computation time for every factor 10 more elements, appears to scale up by a much larger factor than 10!

Going from 1000 to 10000 elements, the input size *N* grows by a factor of 10.
We measured an increase in time from *0.0421* to *4.2984* or a factor of 102,
which seems  closer to a factor of  *100*, or $$10^2$$.

This is because our function `count_occurrence` actually has a quadratic complexity,
denoted as $$O(N^2)$$. This means that as the size of the input for
this function grows by some factor *N*, we expect the computation time to grow
approximately by $$N^2$$.

### Comparing linear and quadratic complexity

Recall that computing the sum of the elements with our linear $$O(N)$$
function for $$10^9$$ elements took about 7 seconds. For the quadratic
`count_occurrence` function, the last measurement we have was for $$10^5$$
elements, taking approximately 4 seconds (on this machine). We can use the
$$O(N^2)$$ complexity of the function to try and estimate how long this
might take for $$10^9$$ elements.

An input size of $$10^9$$ elements would be an increase of a factor $$10^4$$ in
input size compared to $$10^5$$ elements. Given the quadratic complexity, we would expect
a $$(10^4)^2$$ increase in computation time, meaning about *4* seconds *x*
$$10^8$$, which is about **13 years!**

Here we can really see a practical difference between an $$O(N)$$ or an
$$O(N^2)$$ function. For $$10^3$$ elements or less, you probably won't
notice any difference at all, as all computations will be well under 1 second.
For $$10^6$$ it already makes the difference between less than 1 second and
several minutes of waiting for your results. And at $$10^9$$ it is the difference
between a couple of seconds and a completely infeasible couple of years.

Nowadays having millions or more elements in your data set is really quite
common, so knowing the difference between linear and quadratic solutions can
really be critical.

## Constant time

There is one last complexity class we will introduce here, to round out your
perspective on complexity; big $$O(1)$$. Big $$O(1)$$ is also
called *constant time* and it means that the time to compute a function
remains constant as the input grows in size. This is the best possible complexity
any algorithm can have, as it means that the time for the function will remain
roughly the same, even if you have billions of elements to process.

What kind of function could meet this ideal complexity might be hard to
imagine for now, but we'll start with a trivial example. Later in this module we'll see
much more interesting functions with $$O(1)$$ complexity, specifically
when we cover dictionaries. Let's start by considering this simple function, which
always returns the first element from a list:


	def get_first_element(inputs):
		return inputs[0]


	for i in range(5, 9):
		inputs = random_list(10**i)

		elem = timed_function_list(get_first_element, inputs)
		print("The first element was", elem)


	The get_first_element of     100000 elements took 0.000003 seconds to compute.
	The first element was 79
	The get_first_element of    1000000 elements took 0.000003 seconds to compute.
	The first element was 5
	The get_first_element of   10000000 elements took 0.000002 seconds to compute.
	The first element was 58
	The get_first_element of  100000000 elements took 0.000004 seconds to compute.
	The first element was 46


As you can see, getting the first element takes about the same time for each
of these input sizes, even though the inputs get bigger with a factor 10 each
time. This means the function `get_first_element` has a complexity of
$$O(1)$$. So in theory, we could get the first element from a list with
*any* number of elements and it would still only take 0.000004 seconds (although at some point, we might have some trouble fitting that list in our computer's memory).

Next, take a look at the readings on data structures. These readings will not
just cover the operations that a data structure supports, but also what the
complexity is of each of these operations. Many data structures are used *specifically*
because they are more efficient in certain situations.
