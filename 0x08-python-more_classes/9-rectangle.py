#!/usr/bin/python3A
'''
Class that defines a rectangle
'''


class Rectangle():
    '''Class specifications'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            return ("")

        row = str(self.print_symbol) * self.__width
        return ((row + "\n") * (self.__height - 1) + row)

    def __repr__(self):
        '''Displays str rep of instance in developer-friendly way'''
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        '''Handles the deletion of an instance'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
        del (self)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Determines which area is bigger'''
        if (rect_1.__class__.__name__ != "Rectangle"):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (rect_2.__class__.__name__ != "Rectangle"):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() > rect_2.area()) or (rect_1.area() == rect_2.area()):
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        '''Creates a square from a rectangle'''
        return Rectangle(size, size)
