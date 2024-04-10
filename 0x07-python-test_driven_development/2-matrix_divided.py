#!/usr/bin/python3
"""
A module for matrix operation on a 2 dimensional matrix.

Functions:
    matrix_divided: divides all the elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Arguments:
    matrix: a list of integers or floating point numbers
    div: an integer or float to divided the matrix by

    Return:
    a new matrix with all elements divided by 'div'
    """

    new_matrix = []
    err_msg_1 = "matrix must be a matrix (list of lists) of integers/floats"
    err_msg_2 = "Each row of the matrix must have the same size"
    err_msg_3 = "div must be a number"
    err_msg_4 = "division by zero"

    # Check if matrix is a list
    if (type(matrix) is not list):
        raise TypeError(err_msg_1)

    # Check if matrix is a list of lists
    for row in matrix:
        if (type(row) is not list):
            raise TypeError(err_msg_1)

        # Check if matrix is a list of lists of integers/floats
        for ele in row:
            if type(ele) is not int and type(ele) is not float:
                raise TypeError(err_msg_1)

    # Check that the size of the rows in the matrix are equal
    cols = [len(row) for row in matrix]
    for i in range(len(cols) - 1):
        if cols[i] != cols[i + 1]:
            raise TypeError(err_msg_2)

    # Check if div is a number
    if (type(div) is not int and type(div) is not float):
        raise TypeError(err_msg_3)
    # Check if div is zero
    if (div == 0):
        raise ZeroDivisionError(err_msg_4)

    for row in matrix:
        new_matrix.append(list(map(lambda ele: round(ele / div, 2), row)))
    # new_matrix = list(map(lambda row: list(map(lambda ele:
    # round(ele / div, 2), row)), matrix))
    return (new_matrix)
