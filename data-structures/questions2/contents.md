# Complexity questions, part 2

All the code fragments below have a variable `n`. Determine the big O complexity in terms of `n` for these fragments. If for example the big O complexity of an algorithm is quadratic, your answer should be "O(n^2)".

### Question 5

Consider the following pseudo code. Take `n` to be the length of the list.

    while list is not sorted:
        for every element in the list:
            if this element > element to the right:
                swap element with element to the right

<textarea name="form[5]" rows="1" required=""></textarea>


### Question 6

For determining the complexity of the code below you don't need to take the first two lines into account.

    my_set = set([42, 21, 7, 3, 2])
    n = len(my_set)

    # determine complexity of part here below:
    if 14 in my_set:
        print("found :)")
    else:
        print("not found :(")

<textarea name="form[6]" rows="1" required=""></textarea>


### Question 7

For determining the complexity of the code below you don't need to take the first two lines into account.

    my_set = set([42, 21, 7, 3, 2])
    n = len(my_set)

    # determine complexity of part here below:
    for i in range(n):
        if i in my_set:
            print(f"{i}: found :)")
        else:
            print(f"{i}: not found :(")

<textarea name="form[7]" rows="1" required=""></textarea>

### Question 8

For determining the complexity of the code below you don't need to take the first three lines into account.

    n = 10
    set1 = set(range(0, n))
    set2 = set(range(n//2, n + n//2))

    # determine complexity of part here below:
    intersection = set1 & set2
    print(intersection)

<textarea name="form[8]" rows="1" required=""></textarea>

### Question 9

For determining the complexity of the code below you don't need to take the first three lines into account.

    n = 10
    list1 = list(range(0, n))
    list2 = list(range(n//2, n + n//2))

    # determine complexity of part here below:
    intersection = []
    for element in list1:
        if element in list2:
            intersection.append(element)

    print(intersection)

<textarea name="form[9]" rows="1" required=""></textarea>


### Question 10

For determining the complexity of the code below you don't need to take the first three lines into account.

    n = 10
    my_dict = {}
    for key in range(n):
        my_dict[key] = list(range(2 * key, 2 * key + n))

    for i in range(n):
        my_list = my_dict[i]
        if i * 5 in my_list:
            print(i * 5)

<textarea name="form[10]" rows="1" required=""></textarea>
