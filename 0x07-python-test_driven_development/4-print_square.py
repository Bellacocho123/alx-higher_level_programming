#!/usr/bin/python3

""" print sqaure module """


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): size length of the square.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        size = int(size)
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
