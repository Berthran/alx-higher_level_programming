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
    Methods:
        validate_attr : validates an instance attribute for type and value
        area : calculates and returns the area of the rectangle
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes an instance of a rectangle'''
        super().__init__(id)
        self.validate_attr("width", width)
        self.validate_attr("height", height)
        self.validate_attr("x", x, ">=")
        self.validate_attr("y", y, ">=")
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
        self.validate_attr("width", value)
        self.__width = value

    @property
    def height(self):
        '''Retrieves the height of the rectangle'''
        return (self.__height)

    @height.setter
    def height(self, value):
        self.validate_attr("height", value)
        self.__height = value

    @property
    def x(self):
        '''Gets the value of x for a rectangle'''
        return (self.__x)

    @x.setter
    def x(self, value):
        self.validate_attr("x", value, ">=")
        self.__x = value

    @property
    def y(self):
        '''Gets the value of y for a rectangle'''
        return (self.__y)

    @y.setter
    def y(self, value):
        self.validate_attr("y", value, ">=")
        self.__y = value

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

    def area(self):
        '''Calculates the area of the rectangle'''
        return (self.__width * self.__height)

    def display(self):
        '''Displays a rectangle with "#"'''
        rows = self.__height
        cols = self.__width
        if (self.__y != 0):
            print("\n" * (self.__y - 1))
        for i in range(rows):
            print(" " * self.__x + "#" * cols)

    def __str__(self):
        """Print formatted output of the class"""
        return ("[Rectangle] ({}) {}/{} - "
                "{}/{}".format(self.id, self.__x,
                               self.__y, self.__width,
                               self.__height))
