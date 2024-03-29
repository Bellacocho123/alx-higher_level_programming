#!/usr/bin/python3

""" say_my_name module """


def say_my_name(first_name, last_name=""):
    """Prints a name

    Args:
        first_name (str): First name
        last_name (str, optional): Last name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
