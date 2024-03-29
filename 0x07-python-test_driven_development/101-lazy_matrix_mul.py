#!/usr/bin/python3
"""Module for matrix multiplication using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using numpy

    Args:
        m_a (list): List of lists of integers/floats
        m_b (list): List of lists of integers/floats

    Returns:
        int: Result of the multiplication
    """
    return np.matmul(m_a, m_b)
