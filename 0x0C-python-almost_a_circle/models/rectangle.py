#!/usr/bin/python3
'''A Rectangle class that inherits from Base

Class:
    Rectangle : a class to create a rectangle
'''
from models.base import Base


class Rectangle(Base):
    '''A class to create a rectangle

    Attributes:
        width : width of rectangle, private
        height : height of rectangle, private
        x : value of x for the rectangle, private
        y : value of y for the rectangle, private
        '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes an instance of a rectangle'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''Retrieves the width of the rectangle'''
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        '''Retrieves the height of the rectangle'''
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        '''Gets the value of x for a rectangle'''
        return (self.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        '''Gets the value of y for a rectangle'''
        return (self.__y)

    @y.setter
    def y(self, value):
        self.__y = y
