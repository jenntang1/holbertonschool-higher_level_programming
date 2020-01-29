#!/usr/bin/python3
""" 0. If it's not tested it doesn't work """
from models.rectangle import Rectangle
import unittest
import os


class MyTest(unittest.TestCase):
    """ Creating class to test Rectangle class. """

    def setUp(self):
        """ Defaults """
        self.width = 1
        self.height = 1
        self.x = 1
        self.y = 1
        self.id = 1

    def test_all(self):
        """ Checking all attributes """
        test = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(test.id, 5)

    def test_two(self):
        """ Checking two attributess """
        test = Rectangle(1, 2)
        self.assertEqual(test.width, 1)

    def test_three(self):
        """ Checking three attributes """
        test = Rectangle(1, 2, 3)
        self.assertEqual(test.height, 2)

    def test_four(self):
        """ Checking four attributes """
        test = Rectangle(1, 2, 3, 4)
        self.assertEqual(test.x, 3)

    def test_raise_one(self):
        """ Checking width TypeError """
        self.assertRaises(TypeError, Rectangle, ("1", 2))

    def test_raise_two(self):
        """ Checking height TypeError """
        self.assertRaises(TypeError, Rectangle, (1, "2"))

    def test_raise_three(self):
        """ Checking x TypeError """
        self.assertRaises(TypeError, Rectangle, (1, 2, "3"))

    def test_raise_four(self):
        """ Checking y TypeError """
        self.assertRaises(TypeError, Rectangle, (1, 2, 3, "4"))

if __name__ == "__main__":
    unittest.main()
