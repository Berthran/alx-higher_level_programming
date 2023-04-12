#!/usr/bin/python3
'''
Class Inheritance.

A samplification of single inheritance in Python.

Classes:
    Rectangle : creates a rectangle using BaseGeometry class

Typical Example Usage:
    >>> r1 = Rectangle(4, 5)
    >>> print(r1.area())
    20
    >>> print(r1)
    [Rectangle] 4/5

'''

#BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Creates a rectangle using attributes from BaseGeometry.

    Attributes:
        width : width of rectangle
        height : height of rectangle
        integer_validator : validates to be an integer

    Methods:
        area : raises an Exception
    '''

    def __init__(self, width, height):
        '''
        Instantiates class with required attributes.

        Parameters:
            width: width of rectangle (private property)
            height ; height of rectangel (private property)
        '''
        if (not self.integer_validator("width", width)):
            self.__width = width
        if (not self.integer_validator("height", height)):
            self.__height = height

    def area(self):
        '''Computes the area of the rectangle'''
        return (self.__width * self.__height)

    def __str__(self):
        '''Formats print() display for class'''
        width = self.__width
        height = self.__height
        return ("[{}] {}/{}".format(type(self).__name__, width, height))
