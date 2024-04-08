#!/usr/bin/python3
'''
A simple Python module that defines a rectangle using OOP

Class:
    Rectangle: a simple representation of a rectangle using OOP
'''


class Rectangle():
    '''A simple OOP representation that defines a Rectangle'''

    def __init__(self, width=0, height=0):
        '''Initializing the Rectangle Class'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Retrieves the value of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Assigns a new value to width'''
        err_msg_1 = "width must be an integer"
        err_msg_2 = "width must be >= 0"
        if not isinstance(value, int):
            raise TypeError(err_msg_1)
        elif (value < 0):
            raise ValueError(err_msg_2)
        else:
            self.__width = value

    @property
    def height(self):
        '''Retrieves the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets a new height for the rectangle'''
        err_msg_1 = "height must be an integer"
        err_msg_2 = "height must be >= 0"
        if not isinstance(value, int):
            raise TypeError(err_msg_1)
        elif (value < 0):
            raise ValueError(err_msg_2)
        else:
            self.__height = value
