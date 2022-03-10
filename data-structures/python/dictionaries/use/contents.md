# Dictionaries
Dictionaries are one of the fundamental data structures of Python, and
just like lists, they can be used to store several elements together in
one variable. Unlike lists, dictionaries store *mappings* from a key to a
value.

## 1. Basic operations

### Video
Watch this video to learn about dictionaries:

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_80k74cvx&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_zmx8rsom)

### Reading
The difference between dictionaries and lists is that instead of using an index
to access elements, we use a key. Searching for things by their keys is the
main reason dictionaries are used so often and why they are such an efficient
data structure. In a list, if we do not know at what index something is stored
exactly, we would have to loop over the list until we found the matching element, whereas in a dictionary, we can just search by key. More on why this is
efficient later, for now let's just see a simple example.

One way we could use a dictionary is to store the mappings in an actual
English-Spanish translation dictionary. We might have the string "Yes" and we
want to store its Spanish translation:

	KEYS            VALUES
	------------------------
	Yes         :   Si
	No          :   No
	Please      :   Por favor
	Thank you   :   Gracias

Here the English words are the keys and we can easily look up their Spanish
translation in the dictionary.

	Dictionary[Please]
	-> Por favor

The mapping here is from one element to another associated element (its
translation), which we might want to look up. This is generally how
dictionaries are used in Python. Let's take a closer look at the syntax in
Python and some more cases where we might want to use dictionaries.

### creating a dictionary

So, dictionaries are an efficient way to store pairs of variables together. As
another example, we could make a fruit basket and store the quantity we have of the different types of fruit. In our previous example we stored Spanish
translations for English words in our dictionary, and here we are going to
store counts for each type of fruit. Using dictionaries in this way, as a
mapping from elements to some count (or a score), is another very common way to use dictionaries

    >>> basket = {'apple': 4, 'banana': 7, 'orange': 2}
    >>> basket
    {'apple': 4, 'banana': 7, 'orange': 2}

### accessing elements

If we want to know how many apples there are in the fruit basket, we can write

    >>> basket['apple']
    4

The left half of each pair is called the **key** and the right half is called
the **value**. So, here we used the key `'apple'` to find the value `4`. This
syntax is very similar to using square brackets to get elements from a *list*,
but instead of using the **index** to retrieve the element stored at that
place in the list, we use the **key** to retrieve the corresponding **value**
from the dictionary.

### adding items

Using this same syntax, we can add a new *key-value pair*

    >>> basket['strawberry'] = 10
    >>> basket
    {'apple': 4, 'banana': 7, 'orange': 2, 'strawberry': 10}

Or we could use this syntax to modify an existing pair. Let's say we ate one of
the bananas, then we could update the dictionary by writing

    >>> basket['banana'] -= 1
    >>> basket
    {'apple': 4, 'banana': 6, 'orange': 2, 'strawberry': 10}

Each *key* in a dictionary **must** be unique, so if we try to add a *key*
that already exists, we will end up overwriting the corresponding *value*. So,
if we try to add another key for apples, we will just end up replacing the old
pair

    >>> basket['apple'] = 6
    >>> basket
    {'apple': 6, 'banana': 6, 'orange': 2, 'strawberry': 10}
    
Note the order of the elements! Dictionaries remember the order in which items are inserted.

### pitfalls

Note that values **do not** have to be unique, as dictionaries are only a
one-way mapping, so you can only use the *keys* to retrieve the corresponding
*values*, not the other way around. Searching for a pair using the value will
produce a *KeyError*

    >>> basket[2]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 2

because the key `2` does not exist in our basket. The value `2`, does of
course occur in our basket, stored under the key `'orange'`

    >>> basket['orange']
    2

If we try to retrieve the number of *mangoes*, that are not in the basket at all,
we also get a *KeyError*

    >>> basket['mango']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'mango'

### get

Sometimes when we use a key that is not in the dictionary we do not want it to throw an error. But instead return a default value (for example `0`). For this, we can use the `get()` function instead of the square brackets, and as the second argument tell the dictionary what value we want if the key is not present in the dictionary:

    >>> basket.get('mango', 0)
    0

So, now we know that our fruit basket unfortunately contains zero mangoes, but in
many situations this result is much more useful than producing an error.

Note that when an item *is* present in the dictionary `get()` will behave just the same as the square brackets:

    >>> basket.get('apple', 0)
    6
    >>> basket['apple']
    6

It is also important to realize that `get()` **does not add items to the dictionary**. After using `get()` to lookup `'mango'`, it is not added to the dictionary.

    >>> basket.get('mango', 0)
    0
    >>> basket
    {'apple': 6, 'banana': 6, 'orange': 2, 'strawberry': 10}

### in

We can also explicitly ask if a key is present in the dictionary using `in`

    >>> if 'banana' in basket:
    ...   print("We've got bananas!")
    ...
    We've got bananas!

This works exactly the same way as it does for lists. But it only looks at the *keys* of the dictionary. It will not check the *values* of a dictionary. There is one important difference between using `in` with dictionaries and using `in` with lists: With dictionaries `in` is much (!) faster. More about that later.

### looping

Dictionaries are mostly used for look-up operations, but
sometimes you will also want to loop over the elements in your dictionary.
Dictionaries support many of the same operations that lists do. For instance,
you can use `len` to ask how many pairs there are in the dictionary

    >>> len(basket)
    4

We can also use `for` loops with dictionaries, like so

    >>> for fruit in basket:
    ...   print(fruit)
    ...
    apple
    banana
    orange
    strawberry

This will only loop over the keys of the dictionary, but we could just use the
square brackets to retrieve the values as well

    >>> for fruit in basket:
    ...   print(fruit, basket[fruit])
    ...
    apple 6
    banana 6
    orange 2
    strawberry 10

We can even use the `items` function to easily loop over both

    >>> for fruit, amount in basket.items():
    ...   print(fruit, amount)
    ...
    apple 6
    banana 6
    orange 2
    strawberry 10
