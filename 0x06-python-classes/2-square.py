#!/usr/bin/python3
""" class of square initialized with int size """


class Square:
    """ class square """

    try:
        def __init__(self, size=0):
            """instantiates square with size

            Args:
                size - size of the square
            raises:
            ValueError - if size < 0
            TypeError - if value is not an int
            """
            if int(size) < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
    except (TypeError) as e:
        raise TypeError("size must be an integer")
