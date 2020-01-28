#!/usr/bin/python3
""" 0. If it's not tested it doesn't work """
from models.rectangle import Rectangle
import unittest
import random
import os


class MyTest(unittest.TestCase):
    """ Creating class to test Rectangle class. """

    def setUp(self):
        self.id = 1
        self.width = 1
        self.height = 1
        self.x = 1
        self.y = 1

    def test_int_id(self):
        """ Check id is int """
        test = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(test.id, 5)

    def test_int_width(self):
        """ Check width is int """
        test = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(test.width, 1)

    def test_int_height(self):
        """ Check height is int """
        test = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(test.height, 2)

    def test_int_x(self):
        """ Check x is int """
        test = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(test.x, 3)

    def test_int_y(self):
        """ Check y is int """
        test = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(test.y, 4)



if __name__ == "__main__":
    unittest.main()
