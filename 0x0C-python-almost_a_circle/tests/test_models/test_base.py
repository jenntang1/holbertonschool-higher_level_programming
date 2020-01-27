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
        self.assertIsInstance(self.id, int)

if __name__ == "__main__":
    unittest.main()
