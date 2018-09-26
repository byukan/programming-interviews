




import numpy as np

"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangeable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""


class Classy(object):
    def __init__(self):
        self.items = []

    """ takes string as input and adds to items list"""
    def addItem(self, item):
        self.items.append(item)

    """ calc classiness value based on items"""
    def getClassiness(self):
        classiness = 0
        for x in self.items:
            if x == "tophat":
                classiness += 2
            elif x == "bowtie":
                classiness += 4
            elif x == "monocle":
                classiness += 5
        return classiness


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


def transpose(mat):
    """
    INPUT: 2 dimensional list of integers
    OUTPUT: 2 dimensional list of integers

    Return the transpose of the matrix. You can do this using a double for loop in a list comprehension.
    There is also a solution using zip.

    Example:
    # >>> transpose([[1, 2, 3],[4, 5, 6]])
    [(1, 4), (2, 5), (3, 6)]
    """
    return [i for i in zip(*mat)]


def average_rows(mat):
    """
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: list of floats

    Write a list comprehension to take the average of each row in the matrix and
    return it as a list.

    Example:
    >>> average_rows([[4, 5, 2, 8], [3, 9, 6, 7]])
    [4.75, 6.25]
    """
    avgs = []
    for i in range(len(mat)):
        avgs.append(np.mean(mat[i]))

        print(np.mean(mat[i]))
    return avgs


def sort_row(row):
    return sorted(row)


def main():
    print(transpose([[1, 2, 3], [4, 5, 6]]))
    print([(1, 4), (2, 5), (3, 6)])

    assert transpose([[1, 2, 3], [4, 5, 6]]) == [(1, 4), (2, 5), (3, 6)]

    mat = [[4, 5, 2, 8], [3, 9, 6, 7]]

    for i in range(len(mat)):
        mat[i] = sort_row(mat[i])

    mat = sorted(mat, key=lambda i: sort_row(i)[0])
    print(mat)

    # Test cases
    me = Classy()

    # Should be 0
    print(me.getClassiness())

    me.addItem("tophat")
    # Should be 2
    print(me.getClassiness())

    me.addItem("bowtie")
    me.addItem("jacket")
    me.addItem("monocle")
    # Should be 11
    print(me.getClassiness())

    me.addItem("bowtie")
    # Should be 15
    print(me.getClassiness())

    # test 0 items
    you = Classy()
    print(you.getClassiness())


main()
