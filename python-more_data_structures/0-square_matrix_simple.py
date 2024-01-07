#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row for the result matrix
        result_row = []

        # Iterate through each element in the row and square it
        for element in row:
            result_row.append(element ** 2)

        # Add the squared row to the result matrix
        result_matrix.append(result_row)

    # Return the final squared matrix
    return result_matrix
