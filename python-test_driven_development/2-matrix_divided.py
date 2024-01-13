#!/usr/bin/python3
"""The main block of code that is executed
only when the script is run as the main program."""
if __name__ == '__main__':
    """
    The main block of code that is executed
    only when the script is run as the main program.

    This block typically contains code that
    initializes and executes the functionality of the script.
    In this case, it defines a matrix division
    function and demonstrates its usage.
    """

    def matrix_divided(matrix, div):
        """
        Divide each element of a matrix by a given divisor.

        Args:
            matrix (list of lists): The input matrix to be divided.
            div (int or float): The divisor to be used for division.
        """
        new_matrix = []
        """Check to make sure row in matrix is a list"""
        if (not all(isinstance(row, list) for row in matrix)
                or not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        """Each row of the matrix must be of the same size"""
        if len(set(len(row) for row in matrix)) > 1:
            raise TypeError('Each row of the matrix must have the same size')
        """Check to make sure divisor is an integer or a float"""
        if not isinstance(div, (int, float)):
            raise TypeError('div must be a number')
        """Check to make sure divisor is > 0"""
        if div == 0:
            raise ZeroDivisionError('division by zero')
        """Iterate through each row of the matrix
        and store it in a new list"""
        for row in matrix:
            new_row = [round(num / div, 2) for num in row]
            new_matrix.append(new_row)
        """Return a new list of the matrix"""
        return new_matrix
