#!/usr/bin/python3
import sys

sys.path.append("/home/danlinux/new-ALX_SE/alx-higher_level_programming/0x08-python-more_classes")
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 45
my_rectangle.height = 0

print(my_rectangle)
print(repr(my_rectangle))
