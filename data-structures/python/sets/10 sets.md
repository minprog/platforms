# Sets

Sets are an efficient way to store a collection of unique elements and are closely related
to dictionaries. Like dictionaries, they are unordered collections and require
all stored elements to be hashable. However, they merely store elements and
do **not** contain a mapping between keys and values like a dictionary. Instead,
they support some other operations commonly performed with sets, like
intersection.

Learn more about sets with this video:

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_u96n1ef6&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_1k2dy7ii)


Let's take a look at some sets in practice.

Making a set can be done using the same curly braces as a dictionary

	>>> s = {'this', 'is', 'a', 'set'}
	>>> s
	{'a', 'set', 'is', 'this'}

As you can see, sets are unordered like dictionaries. The elements in a set
must also be unique, so if we try to add elements that are already in the set,

	>>> s.add('this')
	>>> s.add('also')
	>>> s.add('this')
	>>> s
	{'is', 'set', 'a', 'this', 'also'}

the set will still only contain one copy of each of those elements.

The most common use for sets is to make a collection of unique elements, by
converting them to a set.

	>>> l = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
	>>> l
	[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
	>>> set(l)
	{1, 2, 3, 4, 5, 6, 9}
	>>> list(set(l))
	[1, 2, 3, 4, 5, 6, 9]

So, turning a list into a set will remove any duplicate elements. You can then
even turn the set back into a list if you need the data in list form instead
of a set. This is generally considered the easiest way to make a list unique.
Note that the order in the list has changed though, as sets are unordered, so
the original order from the list is lost in this conversion.

As you might have noticed, sets share many attributes with dictionaries. Like
dictionaries, they also work based on **hashing**, which means that checking
if an element is in a set is also a constant time $$O(1)$$ operation.

	>>> 'a' in s
	True

So, no matter how many elements in the set, checking if elements are present
will be fast. The fact that sets work with hashing means that they can also
only contain hashable elements, so we cannot add a list as an element:

	>>> s.add([3, 4])
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: unhashable type: 'list'

All this efficient checking if elements are contained in sets
is also used to make the classic set operations very efficient. Set
operations, as described by set theory (a branch of mathematical
logic), concerns which elements are shared between 2 sets. Let's start by making
two sets.

	>>> b = {3, 5, 7, 8, 12, 16, 21}
	>>> b = {16, 24, 21, 8, 9, 1, 2}
	>>> a
	{3, 5, 7, 8, 12, 16, 21}
	>>> b
	{1, 2, 8, 9, 16, 21, 24}

The first operation we'll look at is union, which constructs a new set
containing the unique elements combined from both sets.

	>>> a.union(b)
	{1, 2, 3, 5, 7, 8, 9, 12, 16, 21, 24}
	>>> a | b
	{1, 2, 3, 5, 7, 8, 9, 12, 16, 21, 24}
	>>> b | a
	{1, 2, 3, 5, 7, 8, 9, 12, 16, 21, 24}

We can apply the union operation with the `.union()` function on the sets or
by using the `|` operator between the two sets. Note that the order of the operands
doesn't matter as taking the union between `a` and `b` is the same as taking the
union between `b` and `a`.

Next up, we'll try intersection, which you also already saw in the introduction.
It constructs a new set with the unique elements contained in *both* sets.

	>>> a.intersection(b)
	{8, 16, 21}
	>>> a & b
	{8, 16, 21}
	>>> b & a
	{8, 16, 21}

We can apply the intersection operation with the `.intersection()` function or by
using the `&` operator. As with union, the order between the operands doesn't
matter, as the intersection between `a` and `b` is the same as the intersection
between `b` and `a`.

Finally, let's take a look at set difference:

	>>> a.difference(b)
	{3, 12, 5, 7}
	>>> a - b
	{3, 12, 5, 7}
	>>> b - a
	{24, 1, 2, 9}

So the set difference between `a` and `b` creates a new set with all the
elements from `a` that are **not** present in `b`. Note that the order of the
operands here *does* matter.

We can also check if sets are subsets or supersets of each other, meaning one
contains *all* the elements of the other.

	>>> c = a & b
	>>> c
	{8, 16, 21}
	>>> c.issubset(a)
	True
	>>> c <= a
	True
	>>> c.issuperset(a)
	False
	>>> c >= a
	False
	>>> a >= c
	True

This can be done with the `.subset()` and `.superset()` functions or the `<=`
and `>=` operators. There are also the `<` and `>` operators for *strict*
subsets, meaning the two sets cannot be equal.

This concludes this introduction to sets.
