#!/usr/bin/python3
'''
A module containing a Square class that inherits the methods of the
Rectangle Class which is a subclass of the BaseGeometry class

Classes:
    Square: a class that defines a square
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    A class that defines a square

    Methods:
        init: initializes the class
    '''

    def __init__(self, size):
        '''Initializes the rectangle's width and height

        Parameter:
            size: the length of the square sides
        '''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''
        Computes the area of the square
        '''
        return (self.__size * self.__size)

    def __str__(self):
        '''
        Displays the Square class in a reader frinedly manner
        '''
        class_name = self.__class__.__name__
        return ("[{}] {}/{}".format(class_name, self.__size, self.__size))
