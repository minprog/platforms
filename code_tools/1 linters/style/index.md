# Linters

Consistent code style is tricky on its own. But especially when projects grow or when multiple people start to get involved, it becomes a near impossible task. That is, if there's no one or nothing checking and enforcing it. That is what code linters can do for you.

The name comes from the filter that seperates fluff shed by clothing in a dryer. That filter is called a **lint** trap. The analogy here is, a linter should catch small hard to detect errors that might have a big effect if left unchecked. These tools are not new, likely also not for you. If you've been working in a modern editor like Visual Studio Code for instance, you have probably noticed all sort of hints popping up while programming. That's a linter doing work.

Linters do static code analysis. That is, without actually running the code, find bugs and errors within it. These can be functional errors, like undeclared variables or missing imports. But also non-functional ones, like style errors!

Style is both personal and impersonal. For instance, if you are collaborating you wouldn't want everyone to write code in their own style. Much like other pieces of combined work, like newspapers and magazines, it is probably best to set up some rules for everyone to adhere to: a style guide. But not everything is set in stone, there will always be cases where you as a programmer need to make a judgement call or in some cases might need to diverge from a guide for the sake of readable code.


## PEP 8

Early on the developers of Python set out to create a default style guide for Python in [PEP 8](https://www.python.org/dev/peps/pep-0008/) (Python Enhancement Proposal #8). Take a quick moment to check out the style guide out. It's effectively a set of guidelines to follow and this is also the style guide used for Python's own code. Right at the start of the guide you'll find [the following excerpt](https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds) titled "a foolish consistency is the hobgoblin of little minds":

    Some other good reasons to ignore a particular guideline:

    1. When applying the guideline would make the code less readable, even for someone who is used to reading code that follows this PEP.
    2. To be consistent with surrounding code that also breaks it (maybe for historic reasons) -- although this is also an opportunity to clean up someone else's mess (in true XP style).
    3. Because the code in question predates the introduction of the guideline and there is no other reason to be modifying that code.
    4. When the code needs to remain compatible with older versions of Python that don't support the feature recommended by the style guide.

In other words, it starts with a warning to not blindly follow the guide. And some recommendations if you will, to break guidelines when needed.


## flake8

That said, PEP 8 is very useful. With a standard style guide out there, many have gone out and written code linters that can enforce PEP 8. One such tool is `flake8`. You can install it through `pip`:

    pip3 install flake8

`flake8` can check your code for compliance to PEP 8. Simply call `flake8` in the folder with your code like so:

    $ flake8
    ./foo.py:2:9: E221 multiple spaces before operator
    ./foo.py:3:80: E501 line too long (110 > 79 characters)
    ./foo.py:5:1: E302 expected 2 blank lines, found 1
    ./foo.py:10:25: W292 no newline at end of file

Looks like the code contains some style errors at lines 2, 3, 5, and 9 respectively. With four different error codes, `E221`, `E501`, `E302`, and `W292`. [Here](https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes) is a full list of all the possible error codes. After these error codes there is a short description on what is wrong. So in our case, a couple of blank lines that are missing, a line that is too long, and too many spaces before an operator.

However, the default is probably not what you want. Odds are you, or the existing code before you, might disagree with PEP 8. Line length is a good example here, PEP 8 asks for 79 characters on a line max. This is a hot topic, but as time goes on, longer lines seem to become more acceptable. For instance, GitHub has their code editor show 127 characters per line in their online code editor. If we are going to be hosting our code on GitHub, might as well use their standards like so:

    $ flake8 --max-line-length=127
    ./foo.py:2:9: E221 multiple spaces before operator
    ./foo.py:5:1: E302 expected 2 blank lines, found 1
    ./foo.py:10:25: W292 no newline at end of file

There are many other configurable options to set in `flake8`. For these, you are best of reading [flake8's documentation](https://flake8.pycqa.org/en/3.9.2/index.html). One thing to note is ignorning specific errors. That can either be done globally like so:

    $ flake8 --max-line-length=127 --ignore=E302,W292
    ./foo.py:2:9: E221 multiple spaces before operator

In this case `E302` and `W292` are straight up ignored. In other cases you might want to make a specific exception in a part of the code. That can be done in the code itself through magic comments:

    print("this is a really long line, probably way longer than what it should be, but for now we think this is okay")  # noqa: E501

By appending `# noqa: E501` to the end of the line, `flake8` will ignore this line for `E501`. Do note the double spaces between the comment and the line itself. If curious, noqa stands for No Quality Assurance.


## What to do

Accept [this GitHub Classroom assignment](https://classroom.github.com/a/8sJ_R49R)

Take an old Python assignment of at least `100` LOC (lines of code) and make it compliant with PEP 8. Use `flake8` to check for any style errors. We will check for any type errors with this command:

    flake8 --max-line-length=127

You are free to ignore specific style errors in the code itself through `# noqa`. If you do, briefly elaborate below why you ignored that error.

<textarea name="form[q1]" rows="5" required=""></textarea>

## How to Submit

Submit your repository URL below. This should look something like: `https://github.com/minprog-platforms/your_repo_name`.
