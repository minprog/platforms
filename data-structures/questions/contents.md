# Complexity questions

All the code fragments below have a variable `n`. Determine the big O complexity in terms of `n` for these fragments. If for example the big O complexity of an algorithm is quadratic, your answer should be "O(n^2)".

Hint: If you are not sure, you can run the code yourself and see what happens if you change the variable `n`.

### Question 1

n = 6

for i in range(n):
    print(i)

<text name="form[1]" rows="1" required=""></textarea>

### Question 2

n = 2

for i in range(10):
    print(n + i)

<text name="form[2]" rows="1" required=""></textarea>

### Question 3

n = 5

for i in range(n):
    for j in range(n):
        print(str(i*j) + "\t", end="")
    print()

<text name="form[3]" rows="1" required=""></textarea>

### Question 4

n = 4

for i in range(n*3):
    print(i)

<text name="form[4]" rows="1" required=""></textarea>

### Question 5:

Consider the following pseudo code. Take `n` to be the length of the list.

    while list is not sorted:
        for every element in the list:
            if this element > element to the right:
                swap element with element to the right

<text name="form[5]" rows="1" required=""></textarea>
