#!/usr/bin/python3
""" class of square initialized with int size """


class Square:
    """ class square """

    def __init__(self, size=0):
        """
        instantiates square with size

        Args:
            size - size of the square
        raises:
            ValueError - if size < 0
            TypeError - if value is not an int
        """
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """
        public instance method area

        Args:
            self - instance
        """
        return self.__size ** 2
