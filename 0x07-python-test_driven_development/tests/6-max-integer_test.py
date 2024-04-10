#!/usr/bin/python3
'''
Test module for testing a function using unittest
'''

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_noargument(self):
        result = max_integer()
        self.assertEqual(result, None)

    def test_nonetype(self):
        try:
            max_integer(None)
        except Exception as e:
            self.assertRaises(TypeError, "object of type 'NoneType' has no len()")

    def test_max_beginning(self):
        a_list = [4, 1, 2, 3]
        max_int = max_integer(a_list)
        self.assertEqual(max_int, 4)

    def test_max_mid(self):
        a_list = [1, 2, 4, 3]
        max_int = max_integer(a_list)
        self.assertEqual(max_int, 4)

    def test_max_end(self):
        a_list = [1, 2, 3, 4]
        max_int = max_integer(a_list)
        self.assertEqual(max_int, 4)

    def test_max_duplicate(self):
        a_list = [1, -2, 4, 4]
        max_int = max_integer(a_list)
        self.assertEqual(max_int, 4)

    def test_max_negative(self):
        a_list = [-1, -2, -3, -4]
        max_int = max_integer(a_list)
        self.assertEqual(max_int, -1)

    def test_max_oneelement(self):
        a_list = [4]
        max_int = max_integer(a_list)
        self.assertEqual(max_int, 4)
