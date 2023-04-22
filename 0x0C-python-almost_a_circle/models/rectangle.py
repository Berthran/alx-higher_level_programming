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
        if (not self.validate_attr("width", width)):
            self.__width = width
        if (not self.validate_attr("height", height)):
            self.__height = height
        if (not self.validate_attr("x", x, ">=")):
            self.__x = x
        if (not self.validate_attr("y", y, ">=")):
            self.__y = y

    def validate_attr(self, attribute, value, val_comp=">"):
        '''Validates the type and value of instance attributes'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))
        if (val_comp == ">"):
            if (value <= 0):
                raise ValueError("{} must be {} 0".format(attribute, val_comp))
        if (val_comp == ">="):
            if (value < 0):
                raise ValueError("{} must be {} 0".format(attribute, val_comp))

    @property
    def width(self):
        '''Retrieves the width of the rectangle'''
        return (self.__width)

    @width.setter
    def width(self, value):
        if (not self.validate_type("width", value)):
            self.__width = value

    @property
    def height(self):
        '''Retrieves the height of the rectangle'''
        return (self.__height)

    @height.setter
    def height(self, value):
        if (not self.validate_type("height", value)):
            self.__height = value

    @property
    def x(self):
        '''Gets the value of x for a rectangle'''
        return (self.__x)

    @x.setter
    def x(self, value):
        if (not self.validate_type("x", value)):
            self.__x = value

    @property
    def y(self):
        '''Gets the value of y for a rectangle'''
        return (self.__y)

    @y.setter
    def y(self, value):
        if (not self.validate_type("y", value)):
            self.__y = y
