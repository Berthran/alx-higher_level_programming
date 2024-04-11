#!/usr/bin/python3
'''
Use of NumPy for matrix multiplication

Functions:
    lazy_matrix_mul: multiplies 2 matrices using NumPy
'''

import numpy as np


def is_list(matrix, matrix_name):
    '''
    Function to check if the argument is a list or list of lists
    '''
    if (type(matrix) is not list):
        raise TypeError("{} must be a list".format(matrix_name))

    for row in matrix:
        if (type(row) is not list):
            raise TypeError("{} must be a list of lists".format(matrix_name))


def is_empty(matrix, matrix_name):
    '''
    Function to check if the argument is an empty list
    or empty list of lists
    '''
    err_msg = "{} can't be empty".format(matrix_name)
    if (len(matrix) == 0):
        raise ValueError(err_msg)
    for row in matrix:
        if (len(row) == 0):
            raise ValueError(err_msg)


def is_list_of_integers(matrix, matrix_name):
    '''
    Function to check if the elements of the matrix are either
    floats or integers
    '''
    for row in matrix:
        for ele in row:
            if (type(ele) is not int and type(ele) is not float):
                err_msg = "{} should contain only integers or floats"
                raise TypeError(err_msg.format(matrix_name))


def is_matrix(matrix, matrix_name):
    '''
    Function to check if the argument is a matrix
    '''
    for i in range(len(matrix) - 1):
        if (len(matrix[i]) != len(matrix[i + 1])):
            err_msg = f"each row of {matrix_name} must be of the same size"
            raise TypeError(err_msg)


def is_multiliable(matrix_a, matrix_b, matrix_name_1, matrix_name_2):
    '''
    Function to check if two matrices can be multiplies
    '''
    col_a = len(matrix_a[0])
    row_b = len(matrix_b)

    if (col_a != row_b):
        err_msg = "{} and {} can't be multiplied"
        raise ValueError(err_msg.format(matrix_name_1, matrix_name_2))


def lazy_matrix_mul(m_a, m_b):
    '''
    Function for matrix multiplication

    Parameters:
        m_a: the first matrix
        m_b: the second matrix
    '''
    # Check if the arguments are lists and list of lists
    is_list(m_a, "m_a")
    is_list(m_b, "m_b")

    # Check if any of the arguments are empty
    is_empty(m_a, "m_a")
    is_empty(m_b, "m_b")

    # Check if the lists contains only integers or floats
    is_list_of_integers(m_a, "m_a")
    is_list_of_integers(m_b, "m_b")

    # Check if the list conform to to a matrix
    is_matrix(m_a, "m_a")
    is_matrix(m_b, "m_b")

    # Check if the matrices are multipliable
    # col of m_a == row of m_b
    is_multiliable(m_a, m_b, "m_a", "m_b")

    matrix_prod = np.matmul(m_a, m_b)
    return (matrix_prod)
