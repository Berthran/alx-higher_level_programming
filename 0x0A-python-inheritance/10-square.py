#!/usr/bin/python3
'''
Class Inheritance.

A samplification of multi-level inheritance in Python.

Classes:
    Square : creates a square using Rectangle class

Typical Example Usage:
    >>> r1 = Sqaure(4, 5)
    >>> print(r1.area())
    20
    >>> print(r1)
    [Rectangle] 4/5

'''

Rectangle = __import__('9-rectangle').Rectangle


class Rectangle(Rectangle):
    '''
    Creates a square using attributes from Rectangle.

    Attributes:
        size : length of square
        integer_validator : validates to be an integer

    Methods:
        area : raises an Exception
    '''

    def __init__(self, size):
        '''
        Instantiates class with required attributes.

        Parameters:
            size : length of square
        '''
        if (not self.integer_validator("size", size)):
            self.__size = size

    def area(self):
        '''Computes the area of the square'''
        return (self.__size * self.__size)
