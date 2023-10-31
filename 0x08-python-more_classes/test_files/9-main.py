#!/usr/bin/python3

import sys

sys.path.append("/home/danlinux/new-ALX_SE/alx-higher_level_programming/0x08-python-more_classes")

Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square("7")
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
