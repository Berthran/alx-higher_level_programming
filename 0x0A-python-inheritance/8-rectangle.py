#!/usr/bin/python3
'''Class Inheritance.

Classes:
    Rectangle : creates a rectangle using BaseGeometry class

'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Creates a rectangle using attributes from BaseGeometry'''

    def __init__(self, width, height):
        '''Instantiates class with required attributes

        Parameters:
            width: width of rectangle (private property)
            height ; height of rectangel (private property)
        '''
        if (not self.integer_validator("width", width)):
            self.__width = width
        if (not self.integer_validator("height", height)):
            self.__height = height
