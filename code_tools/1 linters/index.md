# Linters

Consistent code style is tricky on its own. But especially when projects grow or when multiple people start to get involved, it becomes a near impossible task. That is, if there's no one or nothing checking and enforcing it. That is what code linters can do for you.

The name comes from the filter that seperates fluff shed by clothing in a dryer. That filter is called a **lint** trap. The analogy here is, a linter should catch small hard to detect errors that might have a big effect if left unchecked. These tools are not new, likely also not for you. If you've been working in a modern editor like Visual Studio Code for instance, you have probably noticed all sort of hints popping up while programming. That's a linter doing work.

Linters do static code analysis. That is, without actually running the code, finding bugs and errors within it. These can be functional errors, like undeclared variables or missing imports. But also non-functional ones, like style errors!

Style is both personal and impersonal. If you're collaborating you wouldn't want everyone to write code in their own style. Much like other pieces of combined work, like newspapers and magazines, it's probably best to set up some rules for everyone to adhere to: a style guide. But not everything is set in stone, there will always be cases where you as a programmer need to make a judgement call or in some cases might need to diverge from a guide for the sake of readable code.


## PEP 8

Very early on, the developers of Python set out to create a default style guide for Python in [PEP 8](https://www.python.org/dev/peps/pep-0008/) (Python Enhancement Proposal #8). Check the style guide out for a second. It's effectively a set of guidelines to follow and this is also the style guide used for Python's own code. Right at the start of the guide you'll find [the following excerpt](https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds) titled "a foolish-consistency is the hobgoblin of little minds":

    Some other good reasons to ignore a particular guideline:

    1. When applying the guideline would make the code less readable, even for someone who is used to reading code that follows this PEP.
    2. To be consistent with surrounding code that also breaks it (maybe for historic reasons) -- although this is also an opportunity to clean up someone else's mess (in true XP style).
    3. Because the code in question predates the introduction of the guideline and there is no other reason to be modifying that code.
    4. When the code needs to remain compatible with older versions of Python that don't support the feature recommended by the style guide.

In other words, it starts with a warning to not blindly follow the guide. And some recommendations if you will, to break guidelines when needed.


## flake8

That said, PEP 8 is very useful. With a standard style guide out there, many have gone out and written code linters that can enforce PEP 8. One such tool is `flake8`. You can install it through `pip`:

    pip install flake8

