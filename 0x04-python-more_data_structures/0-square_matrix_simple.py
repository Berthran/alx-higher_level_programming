#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    ''' Computes the square value of all integers of a matrix'''
    new_matrix = []
    for row in matrix:
        new_matrix.append([ele**2 for ele in row])
    return (new_matrix)
