# Practice with sets
> **You don't have to hand in these practice exercises.** They're here for you to test yourself. Did you fully understand the theory you just learned?
>
> If there is an exercise that you don't know how to make, review the theory again. If that doesn't help, discuss the exercise with another student and/or the teacher.

Test your understanding with the following practice exercises. Use your usual code editor and create a file called `sets.py`.

**Exercise 1** Create two sets `firstSet` and `secondSet` with the numbers 23, 42, 65, 57, 78, 83, and 29, and 57, 83, 29, 67, 73, 43, and 48 respectively.

**Exercise 2**  Get the intersection of the sets, and save the result in `thirdSet`. Create another set `fourthSet` that holds the difference between `firstSet` and `secondSet`.

**Exercise 3** Add the number 67 to `thirdSet`.

**Exercise 4** Check if `thirdSet` is a subset of `firstSet` and if it is the case print the text "subset!", print the next "not a subset" otherwise.

**Exercise 5** Finally, given the list with double items called `doubles`. Filter for unique items using a set and save the solution as a list in the variable `uniques`.

    doubles = ["tennis", "badminton", "rowing", "soccer", "tennis", "judo", "judo", "karate", "soccer"]
    uniques = # Your solution here

## Solutions
Below you can find some solutions.

> Disclaimer: There are always many ways to solve a problem. The solutions here are not said to be the best solutions.
**Having a different solution, does not necessarily mean it is wrong**.
>
> You should not have to rely on these solutions. If you cannot make the practice exercises at all without looking at these solutions, you should discuss this with your teacher.

<details markdown="1"><summary  markdown="span">Answers</summary>

**Exercise 1**

    firstSet = set([23, 42, 65, 57, 78, 83, 29]) # or firstSet = {23, 42, 65, 57, 78, 83, 29}
    secondSet = set([57, 83, 29, 67, 73, 43, 48]) # or secondSet = {57, 83, 29, 67, 73, 43, 48}

**Exercise 2**

    thirdSet = firstSet & secondSet
    fourthset = firstSet - secondSet

**Exercise 3**

    thirdSet.add(67)

**Exercise 4**

    if thirdSet < firstSet:
        print("subset!")
    else:
        print("not a subset")

**Exercise 5**

    doubles = ["tennis", "badminton", "rowing", "soccer", "tennis", "judo", "judo", "karate", "soccer"]
    uniques = list(set(doubles))

</details>
