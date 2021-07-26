# Static type checking in Python

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_h82tnhqa&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_lphpc5a4)

<https://video.uva.nl/media/Platforms2021%20Typing%20Intro/0_h82tnhqa>

With Python 3.5 came [type hints](https://www.python.org/dev/peps/pep-0484/). A system within Python to *hint* what the type of a variable should be. Probably best explained by a quote from a certain [Disney classic](https://www.imdb.com/title/tt0325980/):

"The code is more what you'd call guidelines than actual rules"

In turn, in Python these hints do not do anything on their own, they are just hints. However there are programs that can take these hints and help you write better code. This is what a type hint looks like in Python:

```Py
def sum(a: int, b: int) -> int:
    return a + b
```

Admittedly the syntax takes some getting used to, but all it says is, here is a function named `add`. `add` takes two integers and will return an integer. Then there are programs such as [mypy](http://mypy-lang.org/) that can take these hints and check whether the program is free of any Type Errors. All before actually running the code.


## Background
<details>
<summary>Types and progamming languages</summary>

Different programming languages have different type systems, but why? Take a quick peek at the example below:


### Python

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_d7kh0wak&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_xty7r3sb)

<https://video.uva.nl/media/Platforms2021%20Typing%20Python/0_d7kh0wak>

```Py
def sum(items):
    total = 0
    for item in items:
        total += item
    return total
```

Python's approach is simple, we'll just run the code and see if it works. If `items` can be summed, then great let's do that. This all works:

```Py
sum([1, 2])
sum([1, 2.0])
sum({1, 2, 3})
```

But this does **not**:

```Py
sum(["hello", 1])
```

And worse yet, we won't know that it does not work until this code is actually run. If the code is not properly tested, then running this function might not happen until its shipped to the client. In which case... **nightmares**.


### C

Okay, but what about other languages? Remember C?

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_4la7ngbg&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_sucghmat)

<https://video.uva.nl/media/Platforms2021%20Typing%20C/0_4la7ngbg>

```C
int sum(int items[], int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += items[i];
    }
    return total;
}
```

C takes a different approach, put a concrete type in front of everything and check it when trying to compile. That way we'll know up front whether the code will even run. Because this:

```C
float array[] = {3.0, 4.0, 5.0};
sum(array, 3);
```

Will nicely throw a compile error. No chance that this code reaches the end user's desk. 

But wait, floats can be summed right? Well, tough luck. You'll need to write a new function for floats.

> For the curious, there are ways to escape C's type system through the use of casting and pointers. Most notably through the use of `void` pointers.

</details>


<details>
<summary>Dynamic vs Static</summary>

All programming languages have some form of type system, but when and what they do with that system varies. First, let's talk about when. There are two main forms, **static** and **dynamic**, and they are not exclusive from one another. 

#### Static

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_lf6czbc1&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_yzi9tqnm)

<https://video.uva.nl/media/Platforms2021%20Typing%20Static/0_lf6czbc1>

Static in this context just means before execution, that could be when compiling the code or through running a seperate type checker. For instance, C makes use of static type checking to ensure that all types operate with one another upon compilation. That way, there is no (technically, little) chance for any type errors while running the program. On top of this compilers can make use of the type information upon compilation to better optimize the resulting program. By for instance reserving precisely enough memory, as the data and their types is know up front.

#### Dynamic

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_bzusnwa5&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_a59l16tx)

<https://video.uva.nl/media/Platforms2021%20Typing%20Dynamic/0_bzusnwa5>

Dynamic means during execution of a program, or in runtime. A good example of a dynamic type system is Python. Values in Python do have types, there are `int`s, `list`s, `string`s, you name it. Misuse of these types will often result in an error, for instance this code:

```Py
"hello" + [1,2,3]
```

Will raise a `TypeError` upon execution. But only during execution. So the information is there, and Python will protect you from weird and unexpected results, but a little late perhaps.

That said, dynamic type systems are often flexible and easy to use. As a programmer you don't have to worry about declaring types, and that means writing less code and probably easier to read code. This is a big reason as to why scripting languages such as Python, JavaScript and Bash tend to favor dynamic type systems. The flexibility in turn makes it possible to do extensive introspection, allowing the program itself to reason about types too. For instance in Python you can check the type of a variable through:

```Py
isinstance(a, int)
```
</details>

<details>
<summary>Type Checking</summary>

Type information can be used for different things, such as optimizing programs, ensuring enough memory is available, but perhaps most important to us programmers: type checking. Ensuring that the program is free of any type errors. 

Type checking can be done both dynamically and statically. But, dynamic type checking happens while running the program and will inevitably impact performance. That is why dynamic type checking is usually only done upon execution of a line of code, to ensure no unnecessary checks are done. That execution of a line of code might be very late, and if you are not testing properly, it might just be in the hands of the end user by the time that buggy line of code finally runs.

In contrast static type checking does not need to worry about performance (as much). Afterall, this style of type checking happens in the developer's time (hence the "as much"), and not the end user's time. This enables a static type checker to do more complex type of checks and give better hints as to what is going wrong. However, to perform static type checking the information on types needs to be available before running the code. That often means that you as a programmer need to add this information. That is both a blessing and a curse. You will have to write more code, but the added information will make it easier for your co-workers or your future self to understand.

Static type checking is often preferred, and so much so that languages such as JavaScript (in the form of TypeScript) and Python have started to adopt type information to enable static type checking. 
</details>


## Type hints in Python

<details>
<summary>Type hints</summary>
A type hint in the simplest form looks like this:

```Py
foo: int
```

All this says is, the type of the variable `foo` should be an integer. Notice how there is no initial value here. This line of code does not create a variable `foo`, all it does is add a hint that `foo`, once it exists, should be an integer. That means this will raise a `NameError`:

```
$ python
>>> foo: int
>>> foo
NameError: name 'foo' is not defined
```

It is possible to combine type hints and initialization on the same line, like so:

```Py
foo: int = 3
```

That looks somewhat redundant, doesn't it? How can the *literal* `3` be anything else than an integer? This is where type inference kicks in. Tools such as `mypy` will try to infer the types of variables from their use. It is quite safe to assume type inference is possible here, so probably best to just write:

```Py
foo = 3
```

Type inference does have its limitations, for instance `mypy` will not do any type inference in functions without type hints. To understand why, let's quickly look into function type hints. In the simplest form:

```Py
def add(a: int, b: int) -> int:
    c = a + b
    return c
```

The syntax is relatively straight forward, using the colon (`:`) for parameter type hints, and the arrow (`->`) for the return type. Notice how the type of `c` is not annotated. It can be, but it is not needed. From the types of `a` and `b` and the `+` operation, `mypy` can infer the type of `c`. But what if we did not annotate this function. Well, in that case, `a` and `b` could be anything: `str`, `float`, `list`, you name it! This is where `mypy` draws a line, if you do not annotate a function, `mypy` will not even attempt to do type inference. Instead all variables will be of type `Any`.

What is `Any`? Well, anything really. It is an escape hatch of sorts that provides no information. Once `Any` gets involved type checking becomes rather impossible. What is `Any + int`? `Any`

</details>

1. Annotate the `factorial` function below:

    ```Py
    def factorial(num):
        total = 1
        for i in range(2, num + 1):
            total *= i
        return total
    ```

    <textarea name="form[q1]" rows="5" required=""></textarea>

<details>
<summary>Generics</summary>

Integers, floats, booleans and strings are primitive data types. Built into the language, they serve as building blocks for more complex data structures. For instance, you might need a `list` to store your data. 

```Py
numbers: list = [1, 2, 3]
number = numbers.pop()
```

Here is the catch, the type `list` does not tell *anything* about what is in the `list`. So really what we have here is a `list` containing `Any`. In this case the type of `number` would be `Any` too.

A `list` is a generic data type. It can store various types, but its operation will vary based on what you store. Simply put for a `list`, if you initially store integers in the list, you will later be able to retrieve integers from that list. This can be annotated as follows:

```Py
numbers: list[int] = [1, 2, 3]
number = numbers.pop()
```

Now `numbers` is defined as a list of integers, and through that `number` will be of type `int` too.

Let's take a quick look at `dict`. Dictionaries are generic over two types, their keys and values. This is how that can be annotated:

```Py
grades: dict[str, int] = {"Martijn": 7, "Marleen": 8}
```

Tuples are an immutable data structure, once initialized it cannot be changed. So it is known up front exactly what the type of each value in the tuple is going to be. Because of this the `tuple` type can a variable amount of generic anotations with exactly as many types as there are values. Like so:

```Py
foo: tuple[int, float] = (7, 7.2)
bar: tuple[int, float, str] = (8, 7.9, "hello world")
baz: tuple[int, int, int] = (1, 2, 3)
```

What about nested data structures?

```Py
stats: dict[str, tuple[int, float]] = {"Martijn": (7, 7.2), "Marleen": (8, 8.1)}
```

Again, in most situations `mypy` can infer the types of the variables, and it is not strictly needed to annotate each data structure for type checking. That said, especially when it comes to data structures, annotations make the code easier to understand.  

</details>

2. Annotate the data structures below:

    ```Py
    foo = ["hello", "world"]
    ```

    <textarea name="form[q2.1]" rows="1" required=""></textarea>

    ```Py
    bar = [("Martijn", 1), ("Marleen", 2)]
    ```

    <textarea name="form[q2.2]" rows="1" required=""></textarea>

    ```Py
    baz = {1: {2: {3: "hello"}}}
    ```

    <textarea name="form[q2.3]" rows="1" required=""></textarea>

<details>
<summary>Type variables</summary>

Generics work through the use of type variables. In Python these variables are provided by `TypeVar` from the `typing` module. Here is how it works:

```Py
from typing import TypeVar

T = TypeVar('T')  # Can be anything
N = TypeVar('N', int, float)  # Must be int or float
```

Type variables can be unconstraint, like `T` above. In this case `T` can be any type at all. Or type variables can be constraint, like `N` above. In which case `N` can only be an `int` or a `float`. Type variables can come in place of actual types. To create for instance generic functions:

```Py
from typing import Iterable, TypeVar

T = TypeVar('T')

def first(items: list[T]) -> T:
    return items[0]
```

`first` will return the first item in the list, but what type is returned is dependent on the list. For instance, if `first` is called like so:

```Py
n = first([1,2,3])
```

Then `n` will be of type `int`. Because a `list[int]` is passed in and `T` will take on the form of `int`. `T` is what is ultimately returned from `first` and that is then why `n` is an `int`.

Type variables can be used outside generic data structures too, for instance:

```Py
def longest(a: T, b: T) -> T:
    return a if len(a) >= len(b) else b
```

This function will work for any type T, and it will return that same type.

</details>

3. Annotate the generic function below with a type variable:

    ```Py
    def repeat(x, n):
        return [x] * n
    ```

    <textarea name="form[q3]" rows="2" required=""></textarea>

## Abstract types

<details>
<summary> Structural subtyping aka duck typing </summary>

So far we have looked at concrete types, such as integers, strings and lists. These types are expressive, you know exactly what you are working with. But, often these concrete types limit design. Take for instance this function:

```Py
def sum(items: list[int]) -> int:
    total = 0
    for item in items:
        total += item
    return item
```

There is no reason this implementation cannot work with other types of data structures. A tuple of integers or a set of integers should work just fine, but the type hint `list[int]` will only accept a concrete `list`. This is quite unpythonic!

Looking at the implementation of `sum`, all that is needed from `items` is that it works with a for-loop. Or more precisely, the data structure needs to be iterable. In this case we only care about a property of the type, not the concrete thing. Rather, if the type we insert into the function is somewhat list-like, the function should work just fine. In comes duck typing:

> if it walks like a duck, swims like a duck, and quacks like a duck... it's a duck.

We need a type that can swim, or in our case a data structure that is iterable. Whether that happens to be a swimming duck or a swimming fish in the end, that is irrelevant here. Luckily Python's `typing` module comes with a bunch of "duck types" built-in, one of which is `Iterable` that we can use like so:

```Py
from typing import Iterable

def sum(items: Iterable[int]) -> int:
    total = 0
    for item in items:
        total += item
    return item
```

Now any calls to `sum`, whether that'd be with a `tuple` or `set`, will all pass type checks. As all of these data structures are iterable! This form of abstract types is called structural subtyping. Alternatively, and probably easier to remember: **static duck typing**. This is done through creating a subtype that only contains some structural aspect of the original type. For instance, `Iterable` is a subtype with only the method `__iter__` (Python's hidden method for iterable things). So as long as the actual type implements `__iter__` any type check will pass.

The `typing` module provides more duck types, most notably: `Sequence` and `Mapping`. `Sequence` is a duck type for anything that keeps an order and is index-able. Lists and tuples are, but a `set` for instance is not.

```Py
from typing import Sequence

a: Sequence[int] = [1, 2, 3]  # All good
b: Sequence[int] = (1, 2, 3)  # All good
c: Sequence[int] = {1, 2, 3}  # Incompatible types in assignment (expression has type "Set[int]", variable has type "Sequence[int]")
```

`Mapping` is a generic type for structures that map one value to another, such as dictionaries for instance.

```Py
from typing import Mapping

a: Mapping[str, int] = {"foo": 1}  # All good
```

<details>
<summary>For the technically curious...</summary>

These abstract data types are implemented as so called `Protocols`. See this [Python Enhancement Proposal](https://www.python.org/dev/peps/pep-0544/). Through these Protocols you can define your own duck types too. For instance:

```Py
from typing import Iterable, Protocol

class SupportsAdd(Protocol):
    def __add__(self, other):
        pass

def sum(items: Iterable[SupportsAdd]) -> SupportsAdd:
    total = None
    for item in items:
        if total is None:
            total = item
        else:
            total += item
    return item

sum([1, 2, 3]) # all good
sum([1.5, None]) # error: List item 1 has incompatible type "None"; expected "SupportsAdd"
```

</details>

</details>

4. Annotate the code below with duck types instead:

    ```Py
    T = TypeVar("T")

    def reverse(items: list[T]) -> list[T]:
        new = []
        for item in items:
            new.insert(0, item)
        return new
    ```

    <textarea name="form[q4.1]" rows="5" required=""></textarea>

    ```Py
    T = TypeVar("T")

    def select(items: list[T], indices: list[int]) -> list[T]:
        selection = []
        for index in indices:
            selection.append(items[index])
        return selection
    ```
    
    <textarea name="form[q4.2]" rows="5" required=""></textarea>


    ```Py
    T = TypeVar("T")

    def filter(items: list[T], allowed: dict[T, bool]) -> list[T]:
        new = []
        for item in items:
            if allowed[item]:
                new.append(item)
        return new
    ```

    <textarea name="form[q4.3]" rows="6" required=""></textarea>

<details>
<summary> Nominal subtyping aka subclassing </summary>

Duck typing is great and all, but what if we actually do want a duck, not something that happens to act like a duck. For instance, let's say we are building a grading app and we have three user roles, `Teacher`, `Assistant` and `Student`. Implemented like so:

```Py
class User:

class Staff(User): pass

class Teacher(Staff): pass

class Assistant(Staff): pass

class Student(User): pass
```

Through this we can write functions that only accept specific types of users. For instance:

```Py
def view_grade(user: User) -> int: pass
def add_grade(user: Staff) -> None: pass
```

This way the type checker will allow all three roles to view grades, but only the `Staff` roles can add a grade. This form of abstract types is called nominal subtyping, where that type or any subclass of that type is accepted.

</details>

<details>
<summary> Special types </summary>

There are some special cases that need special treating and you'll find these in the `typing` module! [Here are the docs](https://docs.python.org/3/library/typing.html#special-forms)

### Union

For instance, in some cases a function might be able to cope with multiple types. Effectively one type or the other. `Union` handles this like so:

```Py
from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b
```

> Starting in Python 3.10, `Union[int, float]` can also be written as `int | float`

### Optional

Sometimes it is uncertain whether a function will return a value. Let's say we are looking for the location of a needle in a haystack. It might be in the haystack, it might also not be. In case it is not, it is a common (not necessarily best) practice to return `None`. That is what `Optional` captures, either a value is returned, or `None`.

```Py
from typing import Optional, Sequence, TypeVar

T = TypeVar("T")

def find_index(haystack: Sequence[T], needle: T) -> Optional[int]:
    for i, hay in enumerate(haystack):
        if hay == needle:
            return i
    return None
```

> `Optional[int]` is equivalant to `Union[int, None]`. In that sense, it is entirely optional to use.

### Callable

Functions can be passed to other functions too. That is what `Callable` captures in Python.

```Py
from typing import Callable

def get_hashes(number: int) -> str:
    return "#" * number

def get_stars(number: int) -> str:
    return "*" * number

def create_pyramid(create_layer: Callable[[int], str], height) -> str:
    pyramid = ""
    for i in range(1, height + 1):
        pyramid += create_layer(i) + "\n"
    return pyramid

print(create_pyramid(get_hashes, 5))
print(create_pyramid(get_stars, 5))
```

</details>

5. Annotate the code below:

    ```Py
    def get(items, index):
        if index >= len(items):
            return None
        return items[index]
    ```

    <textarea name="form[q5.1]" rows="4" required=""></textarea>

    ```Py
    import time

    def pick_one(a, b):
        time_in_milliseconds: int = int(time.time() * 1000)
        if time_in_milliseconds % 2 == 0:
            return a
        return b 
    ```
    
    <textarea name="form[q5.2]" rows="5" required=""></textarea>

    ```Py
    def map(function, items):
        results = []
        for item in items:
            result = function(item)
            results.append(result)
        return results
    ```

    <textarea name="form[q5.3]" rows="6" required=""></textarea>


## mypy

Install `mypy` through pip like so:

```
$ pip install mypy
```

> Depending on your installation, you might need to use `pip3` instead, or `python -m pip`.

Once installed, simply run mypy like so:

```
$ mypy my_program.py
```

Or to type check all python files, use shell globbing or pass a directory instead.

```
$ mypy *.py
$ mypy .
```

To check your answers to the questions above, simply paste them in a Python file and run `mypy` on it. When doing so, be sure to pass in various inputs to the various functions. You can also make use of `reveal_type` to show what type mypy thinks a variable is. Read more about this feature in [the mypy docs](https://mypy.readthedocs.io/en/latest/common_issues.html?highlight=reveal_type#reveal-type).
