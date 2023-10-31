#!/usr/bin/python3
import sys
sys.path.append('/home/danlinux/new-ALX_SE/alx-higher_level_programming/0x08-python-more_classes')
module_name = "1-rectangle"
Rectangle = __import__(module_name).Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.height = -12
my_rectangle.width = 3
print(my_rectangle.__dict__)

my_rectangle.width = 4
my_rectangle.height = 54
print(my_rectangle.__dict__)
