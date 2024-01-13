#!/usr/bin/python3
"""Matrix divide module"""


def matrix_divided(matrix, div):

    new_matrix = []
    """matrix must be a list of lists of integers or floats"""
    if (not all(isinstance(row, list) for row in matrix)
            or not all(isinstance(num, (int, float)) 
                for row in matrix for num in row)):
        raise TypeError('matrix must be a matrix (list of lists)
                of integers/floats')

    """Each row of the matrix must be of the same size"""
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError('Each row of the
                matrix must have the same size')

    """div must be a number (integer or float)"""
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    """div can't be equal to 0"""
    if div == 0:
        raise ZeroDivisionError('division by zero')

    """ All elements of the matrix should be divided by div,
    rounded to 2 decimal places"""
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix
