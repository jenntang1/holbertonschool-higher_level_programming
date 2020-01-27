#!/usr/bin/python3
""" 0. If it's not tested it doesn't work """
from models.base import Base
import unittest
import random
import os


class MyTest(unittest.TestCase):
    """ Creating class to test base class. """

    def setUp(self):
        self.id = 1

    def test_type(self):
        """ Check type is int """
        test = Base(3)
        self.assertIsInstance(test.id, int)

    def test_str(self):
        """ Check type is not str """
        test = Base("string")
        self.assertIsInstance(test.id, str)

if __name__ == "__main__":
    unittest.main()
