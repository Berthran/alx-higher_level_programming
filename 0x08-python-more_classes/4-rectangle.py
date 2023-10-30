#!/usr/bin/python3

class Rectangle():

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Retrieves the width of the recetangle'''
        return self.__width

    @property
    def height(self):
        '''Retrieves the height of the rectangle'''
        return self.__height

    @width.setter
    def width(self, value):
        '''Assigns a new value to width'''
        if (type(value) is not int): 
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        '''Sets a new height for the rectangle'''
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''Computes the area of the rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''Computes the perimeter of the rectanle'''
        return (2 * (self.__width + self.__height))

    def __str__(self):
        '''Depicts the size of the rectangle'''
        if (self.__width == 0 or self.__height == 0):
            return("")
        row_hash = "#" * self.__width
        return ((row_hash + "\n") * (self.__height - 1) + row_hash)

    def __repr__(self):
        '''Shows a string representation of the Rectangle instance'''
        return(f"Rectangle({self.__width}, {self.__height})")
