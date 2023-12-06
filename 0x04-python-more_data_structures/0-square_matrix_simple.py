#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [x for x in map(lambda x: list(map(lambda y: y**2, x)), matrix)]
