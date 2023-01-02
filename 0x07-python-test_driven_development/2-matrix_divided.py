#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Args:
    matrix (list): a list of lists of integers or floats
    div (int or float): the number to divide the matrix by

    Returns:
    list: a new matrix with all elements divided by `div` and rounded to 2 decimal places

    Raises:
    TypeError: if `matrix` is not a list of lists of integers or floats
    TypeError: if any row of the matrix is not of the same size as the first row
    TypeError: if `div` is not a number
    ZeroDivisionError: if `div` is equal to 0
    """

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([[round(item / div, 2) for item in row] for row in matrix])
