#!/usr/bin/python3
'''
A module containing a Rectangle class that inherits the methods of the
BaseGeometry class

Classes:
    Rectangle: a class that defines a rectangle
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    A class that defines a rectangle

    Methods:
        init: initializes the class
        area: computes the area of the rectangle
    '''

    def __init__(self, width, height):
        '''Initializes the rectangle's width and height

        Parameter:
            width: the width of the rectangle
            height: the height of the rectangle
        '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''
        Computes the area of the rectangle
        '''
        return (self.__width * self.__height)

    def __str__(self):
        '''Prints the Rectangle Class in a reader friendly way'''
        class_name = self.__class__.__name__
        return ("[{}] {}/{}".format(class_name, self.__width, self.__height))
