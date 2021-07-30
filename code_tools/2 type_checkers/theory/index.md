# Type checking

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_yhpg39c9&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_fwxn08vn)

<https://video.uva.nl/media/Platforms2021+Typing+Intro+2/0_yhpg39c9>

Python 3.5 introduced [type hints](https://www.python.org/dev/peps/pep-0484/). Syntax within Python to declare what the type of a variable should be. Probably best explained by a quote from a certain [Disney classic](https://www.imdb.com/title/tt0325980/):

"The code is more what you'd call guidelines than actual rules"

In Python these type hints do not do anything on their own, they are just hints. However there are tools that can take these hints and help you write better code. This is what a type hint looks like in Python:


    def add(a: int, b: int) -> int:
        return a + b


Admittedly the syntax takes some getting used to, but all it says is, here is a function named `add`. `add` takes two integers and will return an integer.

Python as a language focuses on writing code easily and quickly. At this point you have probably noticed that you can achieve more with a few lines of Python than let's say a few lines of C. To achieve this, the Python language has to be rather flexible and not all that strict. That does mean however that most bugs and errors are only found while running the program. Forcing you, the programmer, to more carefully test your code. That in itself is not necessarily a bad thing, but it is often difficult to test every part of your program sufficiently. Which in turn leads to bugs lingering in the code. Type hints partially solve this problem, by making it possible to detect type errors early on. Before running your code even!


## Types and progamming languages

Different programming languages have different type systems, but why? Take a quick peek at the example below:


#### Python

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_d7kh0wak&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_xty7r3sb)

<https://video.uva.nl/media/Platforms2021%20Typing%20Python/0_d7kh0wak>


> Note that the TypeError in the video is a runtime error. An error that only pops up when the code is run.


    def sum(items):
        total = 0
        for item in items:
            total += item
        return total


Python's approach is simple, we'll just run the code and see if it works. If `items` can be summed, then great let's do that. This all works:


    sum([1, 2])
    sum([1, 2.0])
    sum({1, 2, 3})


But this does **not**:


    sum(["hello", 1])


And worse yet, we won't know that it does not work until this code is actually run. If the code is not properly tested, then running this function might not happen until its shipped to the client. In which case... **nightmares**.


#### C

Okay, but what about other languages? Remember C?

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_4la7ngbg&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_sucghmat)

<https://video.uva.nl/media/Platforms2021%20Typing%20C/0_4la7ngbg>


    int sum(int items[], int n) {
        int total = 0;
        for (int i = 0; i < n; i++) {
            total += items[i];
        }
        return total;
    }


C takes a different approach, put a concrete type in front of everything and check it when trying to compile. That way we'll know up front whether the code will even run. Because this:


    float array[] = {3.0, 4.0, 5.0};
    sum(array, 3);


Will nicely throw a compile error:


    error: incompatible pointer types passing 'float [3]' to parameter of type 'int *'


No chance that this code reaches the customer's desk! But wait, floats can be summed right? Well, tough luck. You'll need to write a new function for floats.

> For the curious, there are ways to avoid strict typing checking in C too. Through the use of casting and pointers. Most notably through the use of `void` pointers.


## Dynamic vs Static

All programming languages have some form of type system, but when and what they do with that system varies. First, let's talk about when. There are two main forms, **static** and **dynamic**, and they are not exclusive from one another. 

#### Static

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_lf6czbc1&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_yzi9tqnm)

<https://video.uva.nl/media/Platforms2021%20Typing%20Static/0_lf6czbc1>

Static in this context just means before execution, that could be when compiling the code or through running a seperate type checker. For instance, C makes use of static type checking to ensure that all types operate with one another upon compilation. That way, there is no (technically, little) chance for any type errors while running the program. In addition, compilers can make use of the type information upon compilation to better optimize the resulting program. By for instance reserving precisely enough memory, as the data and their types is know up front.

Static type checking is often preferred, and so much so that languages such as JavaScript (in the form of TypeScript) and Python have started to adopt type information to enable static type checking. 

#### Dynamic

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_bzusnwa5&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_a59l16tx)

<https://video.uva.nl/media/Platforms2021%20Typing%20Dynamic/0_bzusnwa5>

Dynamic means during execution of a program, or in runtime. A good example of a dynamic type system is Python. Values in Python do have types, there are `int`s, `list`s, `string`s, you name it. Misuse of these types will often result in an error, for instance this code:


    "hello" + [1,2,3]


Will raise a `TypeError` upon execution. But only during execution. So the information is there, and Python will protect you from weird and unexpected results, but a little late perhaps.

That said, dynamic type systems are often flexible and easy to use. As a programmer you don't have to worry about declaring types, and that means writing less code and probably easier to read code. This is a big reason as to why scripting languages such as Python, JavaScript and Bash tend to favor dynamic type systems. The flexibility in turn makes it possible to do extensive introspection, allowing the program itself to reason about types too. For instance in Python you can check the type of a variable through:


    isinstance(a, int)
