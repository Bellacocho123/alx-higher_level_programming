#!/usr/bin/python3
""" defining a class square """


class Square:
    """class definition """

    def __init__(self, size=0):
        """
        initializimg class

        Args:
            size - of Square

        raises:
            ValueError - if size < 0
            TypeError - if not integer
        """
        self.__size = size

    @property
    def size(self):
        """
        function for size
        """
        return self.__size

    @size.setter
    def size(self, value=0):
        """
        property setter for size

        Args:
            self - instance
            value - of size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current area of a sqaure """

        return self.__size ** 2
