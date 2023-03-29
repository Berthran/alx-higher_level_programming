#!/usr/bin/python3

'''A simple demonstration of Python Class Attributes.
Classes:
--------

    Square

Typical Usage Example:
---------------------

    small_square = Square(1)
    large_square = Square(100)
'''


class Square:
    '''
    A class to create a square

    ...

    Attributes:
    -----------
        size : None
            size of the square

    '''

    def __init__(self, size):
        """
        Constructs all the necessary attributes for a square object.

        Parameters:
        -----------
            size : None
                size of the square
        """

        self.__size = size
