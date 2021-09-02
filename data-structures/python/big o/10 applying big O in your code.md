
# Applying big $$O$$ in your code

This will be the last section on the theory of complexity. Let's first recap what we know. We
discussed 3 complexity classes.

* $$O(1)$$: The fastest, constant time complexity. These are operations
  that are **not** affected by the size of the input at all, and thus will be
  approximately the same speed for *any* size of data.
* $$O(N)$$: The linear time complexity. These operations scale linearly
  with the size of the input. As the complexity for your program as a whole,
  this is very good, but can be too slow for simple parts of your program.
* $$O(N^2)$$: The slow, quadratic time complexity. These operations
  scale quadratically with the size of your input, and thus will be **very**
  slow if your data set is reasonably large.

In addition, we saw many of the built-in data structures for collections of
elements and discussed the complexity of their operations. In particular, we
saw

* **Dictionaries** and **sets**, which are both *unordered* collections of data
  that allow fast $$O(1)$$ checking for the presence of an element using `in`.
  Dictionaries also have $$O(1)$$ complexity for retrieving a value
  associated with a key, e.g. `dictionary[key]`.
* **Lists** and **tuples**, which are both *ordered* collections of data that
  allow for $$O(1)$$ complexity indexing, e.g. `t[5]`, but where many
  other operations like searching with `in` or cutting with slicing actually
  has $$O(N)$$ complexity.
* Lastly, tuples are *immutable*, and can be *hashed*, meaning they can be used in
  sets or as dictionary keys. Lists are *mutable*, not hashable, and thus they
  *cannot* be *hashed*.

## Combining complexities

For now, we have discussed the complexity of individual operations like a
single search or retrieving an index, but your program will most likely
contain **many** of these operations. So how do all these individual
complexities combine to give the complexity of a whole program? There are a
couple rules you should keep in mind to determine the complexity of a whole
program.

## 0. Definition

Let's start with a *slightly* more formal definition: The big $$O$$
notation is a worst case measure of complexity as a function of the size of the
large inputs. Taking our `in` operation on a list as an example again, it
could be that the element we are looking for is at the front of our list and
the search would be very fast. However, in the worst case the element is all
the way at the back, or not even in the list at all, and in both those cases we
would have to check *every* element in the list.

## 1. Constant factors don't matter

When you combine complexities, constant factors can be dropped.

	def first_elem_add(input_list, elem):
		x = input_list[0]
		return x + elem

This function contains 4 $$O(1)$$ operations; an assignment, index
retrieval, an addition and a return. You might therefore argue that the
complexity of this function should be $$O(4)$$, but the constant factor
of 4 can be dropped and the complexity simplified back to $$O(1)$$.

This is because for the complexity class we are only interested in how the amount
of computations *changes* with the size of the input. The amount of computations
here is completely independent of the size of `input_list`, and so will not change
if the `input_list` gets larger by *any* factor. Whether the fixed amount of
computations is 4 or 1 does not matter for the complexity class, the computation
time remains the same and so is multiplied by $$O(1)$$ for any factor increase
in the input size.

The big $$O$$ notation always depends on the size of the input considered,
specifically what happens with very large inputs. As an input gets more massive,
any constant multiplication becomes less and less relevant for the computation
time, as it gets relatively smaller. Any constant multiplication (that does not
depend on the size of the input) of the complexity can always be removed, so
any operation that always has the same amount of time or steps, gets simplified
to $$O(1)$$.

The same simplification can be done with $$O(N)$$ complexities. Let's take a look at the example function below. It checks if an element is present in the list, and if so, finds the index of that element and slices the list right before the found element, cutting off the rest of the list.

	def find_slice(input_list, elem):
		if elem in input_list:
			ind = input_list.index(elem)
			return input_list[:ind]
		else:
			return input_list

Analyzing the complexity here is a little harder, as there is an `if` statement in the code. Let's start working from the definition again; the big $$O$$ notation is a worst case measure of complexity. So what would be the worst case input in this case? If the element
*is* in the list, then the first half of the if will be executed, which is clearly slower and therefore worse. Then, if the element is actually at the very end of the list, then both finding the index and the slicing would need to go through all elements in the list.

So, in the worst case we have 3 $$O(N)$$ operations; a search with `in`,
finding the index and slicing the list. This does not combine to
$$O(3N)$$, but again simplifies back to $$O(N)$$ with the
constant factor of 3 dropped. As the inputs for this function get bigger, the time
the function takes will still scale linearly.

## 2. Only the slowest part matters

When you add several operations with a different complexity together, only the slowest complexity matters. This is closely related to the previous rule, but has a slightly different effect

	def index_increment(input_list, elem):
		ind = input_list.index(elem)
		return ind + 1

This function has an $$O(N)$$ operation to find the index of an
element and 3 $$O(1)$$ operations; assignment, addition and returning.
The resulting complexity is not $$O(N +3)$$ or $$O(N +1)$$,
but just $$O(N)$$.

As the big $$O$$ notation concerns *very large* inputs, the slowest part of the
complexity will always end up having a *much* bigger influence on the computation
time. So, if you have an $$O(N)$$ operation followed by an
$$O(N^2)$$ operation, then the complexity of the whole program is not
$$O(N +N^2)$$, but just $$O(N^2)$$ as determined by the slower
second part. For an input size *N* of 2, the $$O(N)$$ part in the total $$O(N +N^2)$$ complexity would still have an impact, but the bigger *N* gets, the larger the effect of the $$O(N^2)$$ complexity. Therefore, when adding  operations with a different complexity together, this gets simplified to just the slowest complexity.

These slow parts that end up determining the complexity of the whole program
are the "bottlenecks" of the program. These are the parts that will really
hinder performance as the inputs get larger. Finding and identifying these
bottlenecks is the first part of writing efficient code, as you then know what
parts to *improve.*

## 3. Nested complexities multiply

When an operation is nested inside a loop, it gets a bit trickier: the complexity of the operation is multiplied with that of the loop. Repeating an $$O(N)$$ operation *N* times
inside a loop will have an $$O(N \times N)$$ or $$O(N^2)$$
complexity.

You might have already guessed that repeating slow operations inside a loop
will be *very* slow, but now you have a more complete tool to express and
analyze this. Let's take a look at our original example for $$O(N^2)$$,
the function that would count how often each element occurred in the input.

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

Here we have an inner loop (starting at line 6) going over all *N* elements in
the inputs list. The inside of the inner loop (line 8 and 9) only does simple
comparison and some computation, so that part combines to $$O(1)$$. The
$$O(1)$$ inside is repeated *N* times inside the inner loop, so the
total complexity for the inner loop is $$O(N)$$.

That inner loop itself is then repeated *N* times in the outer loop (line 3), once for
each element in the `inputs`. The combined complexity for the outer loop is
therefore *N x N*, so $$O(N^2)$$. Then, there is an assignment at
the start of the function and return at the end, both $$O(1)$$, which
can be dropped as they certainly won't be the slowest part of the computation.

So, the resulting complexity for this function does indeed come out to
$$O(N^2)$$, as was concluded from the timing tests, where for every factor of 10 by which the input got bigger, the function approximately took $$10^2 = 100$$ times longer to compute.

	The count_occurrence of        100 elements took 0.000427 seconds to compute.
	The number 72 occurs 1 times
	The number 11 occurs 1 times
	The number 16 occurs 2 times
	The number 50 occurs 2 times
	The number 67 occurs 1 times
	The count_occurrence of       1000 elements took 0.040301 seconds to compute.
	The number 81 occurs 10 times
	The number 36 occurs 12 times
	The number 51 occurs 8 times
	The number 45 occurs 14 times
	The number 91 occurs 10 times
	The count_occurrence of      10000 elements took 4.051783 seconds to compute.
	The number 10 occurs 93 times
	The number 18 occurs 114 times
	The number 89 occurs 115 times
	The number 68 occurs 99 times
	The number 19 occurs 97 times

Note that all these multiplications do also follow the rules of big
$$O$$ from above, so not all loops will multiply the complexity in the
same way. If a loop repeats something a constant number of times, that does
**not** vary with the size of the input, then the looping complexity would still be
constant $$O(1)$$. So then whatever the complexity is inside the loop,
just gets multiplied by *1* and thus stays the same, as long as the number of
repetitions in the loop does not grow with the size of the input.

Same thing applies to loops that only do *N/2* repetitions or *3N*, both will
just multiply the inner complexity by *N*, with the constant factor dropped.
All that matters is that a loop scales linearly with the size of the input. It is
also possible to make more complex looping structures that would multiply by
$$N^2$$ or even something like $$2^N$$, so consider how many steps your loop is
approximately taking when determining the complexity. Although in general, a
simple loop over the input will just multiply the inner complexity by *N*.

From this rule we can deduce that all slow complexities in programs come from
repeating some more expensive operation *many* times, in some form or another.
Therefore, when trying to make a program *faster* there are 2 things we could
try and do:

1. Reduce how many times the expensive operation needs to be repeated
2. Create a new version of the same expensive operation that is more efficient.

This might seem like obvious suggestions, but finding a way to actually do this
for a program can be *hard*. However, with all this covered, we should have all
the necessary tools to make our `count_occurrence` function **much** faster.
Let's give it a try.
