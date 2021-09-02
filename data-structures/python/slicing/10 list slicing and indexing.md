
# List slicing and indexing

Here we will cover some more things about lists, including slicing and
indexing. Let's dive right in.

A slice is used to *cut* a section out of a list, as the name might imply.
Instead of using an index to retrieve an individual element from a list, we can
use slices to retrieve a section from one index to another:

	>>> l = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
	>>> l
	[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
	>>> l[1]
	1
	>>> l[5]
	9
	>>> l[1:5]
	[1, 4, 1, 5]

Note that the *left index* of the slice **is** included in the slice and the
*right index* of the **isn't** included in the slice. This is because the slice
only goes *up to* the right index.

If we leave out the left or right index in a slice, they default to the start
and end of the list respectively.

	>>> l[:5]
	[3, 1, 4, 1, 5]
	>>> l[5:]
	[9, 2, 6, 5, 3]

The first slice makes a new list from the start of the old list *up to* index
`5`. The second slice makes a new list starting at index `5` until the end
of the list. So here we have sliced the list in half, with half the elements
landing in the first slice and the other elements ending up in the second
slice.

We can also use this to easily make a copy of the list:

	>>> l[:]
	[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

This is a new list containing the old list from the start until the end, so it
is an exact copy. When might you want to use this? Well, you might have already run
into this problem before.

	>>> m = l
	>>> m
	[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
	>>> m[1] = 0
	>>> m
	[3, 0, 4, 1, 5, 9, 2, 6, 5, 3]
	>>> l
	[3, 0, 4, 1, 5, 9, 2, 6, 5, 3]

If you define a list as equal to another list, they actually **are** the same list, as they will point to the same place in memory. Changing one list will actually change the shared memory for *both* lists, and so the other list will also change. If instead, we make a copy of the list using a *slice*, then we actually have a new list with its own copy in memory to work with, so changing one will leave the other the same.

	>>> n = l[:]
	>>> n[2] = 0
	>>> n
	[3, 0, 0, 1, 5, 9, 2, 6, 5, 3]
	>>> l
	[3, 0, 4, 1, 5, 9, 2, 6, 5, 3]

This problem of shared memory is called **pass-by-reference** and it actually
applies to all *mutable* collections of data. Anything more complex than an
integer or a float, like lists or dictionaries, will need to be copied if you
want to modify the copy but keep the original intact.

Now that you understand that the slice operation actually makes a new piece of
memory, you might also better understand its complexity. Slicing has a
complexity of $$O(N)$$, so even if it looks simple and doesn't contain
any loops, it can be quite an expensive operation.

A slice like `[1:]` therefore does not "cut off the first element", but actually
copies all the elements after index `1` to a new list, meaning it is a linear
$$O(N)$$ complexity operation. In contrast, indexing a list with just
`[1]` would always be a constant time $$O(1)$$ complexity operation. A
small change in the syntax can actually make a big change in complexity!

Lists have quite a few of these deceptively simple looking operations that
actually have $$O(N)$$ complexity.

	>>> l
	[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
	>>> 5 in l
	True
	>>> l.index(4)
	2

Any searching operation in a list, so using `in` or trying to find the place of an element
using `.index()`, will be an $$O(N)$$ operation, as it will
actually have to go through the elements one-by-one and compare them. So, even
simple `if` statements like `if x in l` can have $$O(N)$$ complexity
without explicitly looping over the list.

Single instances of these $$O(N)$$ operations might not be so bad, but
if you end up repeating them many times in a loop, it might start to add
up. If you find yourself doing many `in` operations in a loop then you should
always consider if you shouldn't use a *dictionary* or *set* instead. There will
be more on combining complexities in the *Applying Complexity* section, which
will be up next.

But before you read that, let's add one more useful feature for slices; skip
slicing.

	>>> l[3:9]
	[1, 5, 9, 2, 6, 5]
	>>> l[3:9:2]
	[1, 9, 6]
	>>> l[3:9:3]
	[1, 2]

In addition to specifying a start and end point for a slice, we can use a
second `:` to specify the size of the step between elements. Step size `2`
skips 1 element each time, step size `3` skips 2 elements and so on.

	>>> l[::3]
	[3, 1, 2, 3]
	>>> l[::-1]
	[3, 5, 6, 2, 9, 5, 1, 4, 1, 3]

We can actually combine this with leaving out the start and/or end point of the
slice, so taking the full list and skipping 2 elements each time. Skip slicing
even supports *negative* step sizes, so going from the back of the slice to the
front. The most common way you'll see this, is to **reverse** a list completely
with just a slice, so a step size of `-1` for the full list.

Finally, although this whole text has been about lists, it is important
to note that slicing works exactly the same for the other *ordered*
collections, so strings and tuples. Any built-in element that uses *indexing*
to access its elements will usually also support slices.

That completes this reading on slicing and indexing. Up next is the final section
on complexity in this series, about how to combine all this into an efficient
program.
