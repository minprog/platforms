# Example: Improving count_occurrence()

Writing efficient code can be tricky and will take practice, but here we will
try and walk you through the process step by step. If at any point you think
you have an idea for a more efficient version of `count_occurrence`, feel free
to stop reading and try to write it out first, so you can get a head start on
practicing.

Solving a problem efficiently usually requires taking a step back and asking
some questions:

1. What *exactly* is the problem we are trying to solve?
   * We are trying to count how often each element occurs in the list `inputs`.
2. What do we *definitely* need to do to solve the problem?
   * We will **have to** loop over every element at least once, in order to
     include everything in the count correctly.

From this we can conclude that we will definitely need the *outer* loop and it cannot be
reduced, as it will be necessary to visit every element once. So, we should try
to reduce the *inner* loop, where we try to make the count for each number.

	def count_occurrence(inputs):
		counts = []
		for elem_1 in inputs:
			c = 0
			for elem_2 in inputs:
				if elem_1 == elem_2:
					c += 1

			counts.append(c)
		return counts

Our first idea might be to avoid counting elements that have already been
counted, as repeating that for *every* element seems a bit inefficient. So we
could only do the inner loop `if` the element has not been counted yet. While
this might make the code a *bit* faster in most cases, it does not actually
reduce the *worst case* complexity of the code at all. The worst case would
then be that every element is unique and therefore we would still need to do
the complete inner loop for *every* element, resulting in a count of 1 for each
and our same $$O(N^2)$$ complexity.

Avoiding recounting would therefore be a bit better, but not the kind of speed
up we are after in this exercise. So we will have to change the way the counts
are computed in some more fundamental way. Get a pen and paper, write down a
list of numbers and try to count how often each element occurs while going
through the list just once. If we can figure out an efficient strategy, then
maybe we can implement this in *Python* too.

A good solution might be to simply write down a number when you first encounter it
and add 1 mark next to it. The next time you encounter that same number, just
add another mark. This way, after going through the list *once*, the number of
marks next to each number should be equal to their count. Great, but then the
problem just becomes: How do we know if we've already seen a number? If we have
already seen it, how do we know at what place to add the mark? And we have to, of
course, do all this **without looping through the list again**, as that would
basically give us the same $$O(N^2)$$ solution as before.

As a general tip, any time you are trying to make some code more efficient,
changing the structure of the data to something that would make the individual
operations faster is very often a good idea. So, what we would often need to do
is see if an element is *contained* in the collection and if so, *find*
some value associated with it. What data structure have we seen that makes
exactly those 2 operations efficient?

If you answered *dictionary*, then you were correct! We could use the `in`
operation to see if we have already added an element as a *key* to the
dictionary. Then, the associated *value* of that key could keep track of the
count for that element and we could use the square brackets to efficiently
retrieve it. So, in a dictionary both of these operations would actually have
$$O(1)$$ complexity! Let's take a look at the code for this new
version

	def count_occurrence_v2(inputs):
		counts = {}
		for elem in inputs:
			if elem in counts:
				counts[elem] += 1
			else:
				counts[elem] = 1

		return counts
