#!/usr/bin/python3

"""A demonstration of Python Class methods.
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
        size : int, optional
            size of the square
        position : int tuple, optional
            sets the position of the square

    Methods:
    --------
        area
            calculates and returns the current square area

        my_print
            represents a square with "#"s

    """

    def __init__(self, size=0, position=(0, 0)):
        """Constructs all the necessary attributes for a square object.

        Parameters:
        -----------
            size : int, optional
                size of the square
            position : int tuple, optional


        Raises:
        -------
            TypeError : if 'size' is not an integer
            ValueError : if 'size' is less than 0
        """

        self.__size = size
        self.__position = position
        errmsg = "position must be a tuple of 2 positive integers"

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        if (type(self.__position) is not tuple or len(self.__position) != 2):
            raise TypeError(errmsg)
        for i in self.__position:
            if (i < 0):
                raise TypeError(errmsg)

    @property
    def size(self):
        """Retrieves the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the postion of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        errmsg = "position must be a tuple of 2 positive integers"
        if (type(value) is not tuple or len(value) != 2):
            raise TypeError(errmsg)
        for i in value:
            if (i < 0):
                raise TypeError(errmsg)
        self.__position = value

    def area(self):
        """Calculates and returns the current square area."""
        return (self.__size ** 2)

    def my_print(self):
        """Displays the square with '#'s"""
        if (self.__size == 0):
            print("")
        else:
            for i in range(self.__size):
                print(f"{' ' * self.__position[0] + '#' * self.__size}")
