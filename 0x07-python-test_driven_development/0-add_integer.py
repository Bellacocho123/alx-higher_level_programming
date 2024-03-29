#!/usr/bin/python3
""" function to add two integers """


def add_integer(a, b=98):
    """ my addition function
    Args:
        a - integer or float input
        b - integer or float input

    raises:
        TypeError: if a or b not integer or float
        TypeError: if no argument is passed to a
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    a = int(a)
    if a is None:
        raise TypeError("add_integer() missing 1 required positional argument: 'a'")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)

    return (a + b)
