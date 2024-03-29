#!/usr/bin/python3

""" matrix module """


def matrix_divided(matrix, div):
    """ matrix_divided

    Args:
        matrix (list): matrix to be divided
        div (int or float): number to divide by

    Raises:
        TypeError: div must be a number
        ZeroDivisionError: division by zero
        TypeError: = matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size

    Returns:
        list: new matrix
    """

    new_matrix = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int and type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[i]) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if len(matrix[i]) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_matrix.append(list(map(lambda x: round(x / div, 2), matrix[i])))
    return new_matrix
