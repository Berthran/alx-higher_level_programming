#!/usr/bin/python3

"""A demonstration of Python Class Attributes II.
Classes:
    Square

Typical Usage Example:
    mySquare = Square()
    mySquare = Square(10)
"""


class Square:
    """
    A class to create a square.

    ...
    Attributes:
        size : (int, optional)
            size of the square

    """

    def __init__(self, size=0):
        """Constructs all the necessary attributes for a square object.

        Parameters:
        -----------
            size : (int, optional)
                size of the square

        Raises:
        -------
            TypeError : if 'size' is not an integer
            ValueError : if 'size' is less than 0
        """

        self.__size = size

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
