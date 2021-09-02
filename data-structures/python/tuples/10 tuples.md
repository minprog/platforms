# Tuples

## Video
![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_wlxgk3ja&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_dztdpgtv)

## Reference
Tuples are very much like lists, as they store sequences of elements, but they
tend to be used quite differently. The important difference for tuples is that
they are immutable, which means they can support some operations that lists
don't (and vice versa). We'll dive more into what this difference is by looking
at some examples.

Creating a tuple is very similar to creating a list, except we use rounded
brackets instead of square brackets

	>>> t = (42, 'hello', 3.1415)
	>>> t
	(42, 'hello', 3.1415)

We can access elements from a tuple at a specific index with square brackets
just like with a list

	>>> t[1]
	'hello'

However, when we try to assign to an index, like with a list, we get an error

	>>> t[1] = 9
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'tuple' object does not support item assignment

This is the first sign of the fact that the tuple is indeed immutable; it is
*not* possible to change a value at a specific index. In addition to this, we
cannot append things to a tuple either

	>>> t.append('world')
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	AttributeError: 'tuple' object has no attribute 'append'

So, once a tuple is created, we cannot change the elements it contains or add
more elements. This what it means to be immutable; it *cannot be mutated* or
changed at all.

With all these restrictions, it might seem like a tuple just does a lot less
then a list, but immutability also has some advantages.

One of the most common ways a tuple is used, is returning multiple values from
a function.

	>>> def find_max_index(l):
	...     max_ind = 0
	...     max_val = 0
	...     for i in range(len(l)):
	...         if l[i] > max_val:
	...             max_val = l[i]
	...             max_ind = i
	...     
	...     return (max_ind, max_val)
	...
	>>> list_of_values = [4.14, 8.1, 9.7, 2.0]
	>>> find_max_index(list_of_values)
	(2, 9.7)

This function tries to find the maximum value in a list. However, it does not
just return the maximum value, it also returns the index of that maximum value
in the list. Both values are returned together in a tuple.

When you combine several things with commas in between, they automatically
become a tuple, even without the round brackets around it. This is called
tuple *packing*. The last line of the function could, therefore, also have been
`return max_ind, max_val` which is the form you will see more often.

	>>> maximum_index, maximum_value = find_max_index(list_of_values)
	>>> maximum_index
	2
	>>> maximum_value
	9.7

We can see this same thing also works in reverse, when assigning to variables.
Here we assign to 2 new variables `maximum_index` and `maximum_value` in just 1
line. This is called tuple unpacking and assigns the values from the tuple to
the variables in the same order as they were in the tuple.

The number of elements must, therefore, match however many variables you are
trying to unpack.

	>>> t
	(42, 'hello', 3.1415)
	>>> a, b = t
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: too many values to unpack (expected 2)
	>>> a, b, c, d = t
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: not enough values to unpack (expected 4, got 3)
	>>> a, b, c = t
	>>> a
	42

When unpacking a tuple, the number of elements must match exactly and we end
up giving every element a different variable name. This should start to give
you an idea of how and when tuples are used versus lists. If we have some large
number of the same type of thing, all stored together, you would store them in
a list. That way, you can append new elements, loop over each element and
process them all the same way.
If, however, you have a small fixed number of different things you want to store
together, like a maximum value and its index, then you would use a tuple. You
can then return these things, pass them to a function, or even store several of
them in a list, but the items will remain together, unchanged, in the tuple.
Things stored together in a tuple should always be able to be unpacked; you
should know exactly how many elements you are expecting to be in the tuple and
what different things are stored at each index.

The main purpose of tuples, therefore, is storing a small fixed number of
different things together in one structure. There is one other important
application of tuples which we haven't discussed yet; **hashing**. Hashing is
the underlying magic that makes dictionaries so efficient. In the previous text
we talked about the fact that searching for keys in dictionaries was just about
always a constant time $$O(1)$$ operation. Dictionaries achieve this by a
process called *hashing* of the key, which is some computation that tells the
computer where in the dictionary to look for the key. In Python, the hashing
operation is only allowed to be performed with **immutable** elements because,
if we could change a key, then hashing might give a different location to search
after a key was changed, making it impossible to find back. If we try to create
a dictionary with a list as a key, which is of course mutable, we get an error:

	>>> phonebook = {}
	>>> john = ['John', 'Smith']
	>>> phonebook[john] = 5551234
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: unhashable type: 'list'

In this example, we are trying to create a phone book where we can look up
someone based on their first name and last name, and get back their phone
number. But by storing the first name and last name together in a list, we have
created a mutable key, which cannot be hashed. If however we change this to a
tuple, which is immutable, we *can* use the two names together as a key.

	>>> john = tuple(john)
	>>> john
	('John', 'Smith')
	>>> phonebook[john] = 5551234
	>>> phonebook
	{('John', 'Smith'): 5551234}

Storing several things together as a dictionary key is quite common and is
another situation in which you really need a tuple and cannot use a list.

This concludes this introduction on tuples.
