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

    def test_int(self):
        """ Check id is int """
        test = Base(3)
        self.assertEqual(test.id, 3)

    def test_str(self):
        """ Check type is not str """
        test = Base("string")
        self.assertIsInstance(test.id, str)

    def test_None(self):
        """ Check for None """
        test = Base(None)
        self.assertIsNotNone(test.id)

if __name__ == "__main__":
    unittest.main()
