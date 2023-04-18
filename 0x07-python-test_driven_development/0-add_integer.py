#!/usr/bin/python3
''' Addition of two numbers

Functions:
    check_num_types : validatess the type of two numbers
    add_integers: adds two numbers
'''


def check_num_type(num1, num2, dtype=[int, float]):
    '''Validates the type of two numbers

    Arguments:
        num1 : first number
        num2 : second number
        dtype : expected types for num1 and num2

    Return:
        0 if both type checks are successful
        an alphabet corresponding to the position
        of the number with a type failure
    '''

    checklist = [1, 1]
    a_type, b_type = type(num1), type(num2)
    if (a_type is dtype[0] or a_type is dtype[1]):
        checklist[0] = 0
    if (b_type is dtype[0] or b_type is dtype[1]):
        checklist[1] = 0
    if (checklist == [0, 0]):
        return (0)
    if (checklist[0] != 0):
        return ("a")
    if (checklist[1] != 0):
        return ("b")


def add_integer(a, b=98):
    ''' Adds two integers
    Parameters:
        a : first integer
        b : second integer
    Return:
        Sum of a and b
    '''
    num_type = check_num_type(a, b)
    if (num_type != 0):
        raise TypeError("{} must be an integer".format(num_type))
    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)
    return (a + b)
