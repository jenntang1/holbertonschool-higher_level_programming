#!/usr/bin/python3
""" 0. If it's not tested it doesn't work """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import os


class MyTest(unittest.TestCase):
    """ Creating class to test base class. """

    def setUp(self):
        """ Default """
        Base.__nb_objects = 1

    def test_id(self):
        """ Checking that an id is assigned """
        test = Base()
        self.assertEqual(test.id, 1)

    def test_int(self):
        """ Saving id """
        test = Base(3)
        self.assertEqual(test.id, 3)

    def test_plus_one(self):
        """ Saving id + 1 """
        test = Base(+ 1)
        self.assertEqual(test.id, 1)

    def test_to_json_None(self):
        """ Checking to_json_string is None """
        test = Base.to_json_string(None)
        self.assertEqual(test, "[]")

    def test_to_json_empty(self):
        """ Checking to_json_string is empty """
        test = Base.to_json_string([])
        self.assertEqual(test, "[]")

    def test_to_json_works(self):
        """ Checking to_json_string works """
        test = Base.to_json_string([{'id': 12}])
        self.assertEqual(test, '[{"id": 12}]')

    def test_to_json_returns(self):
        """ Checking to_json_string returns """
        test = Base.to_json_string([{'id': 12}])
        self.assertIs(type(test), str)

    def test_from_json_None(self):
        """ Checking from_json_string is None """
        test = Base.from_json_string(None)
        self.assertEqual(test, [])

    def test_from_json_empty(self):
        """ Checking from_json_string is empty """
        test = Base.from_json_string("[]")
        self.assertEqual(test, [])

    def test_from_json_works(self):
        """ Checking from_json_string works """
        test = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(test, [{"id": 89}])

    def test_from_json_returns(self):
        """ Checking from_json_string returns """
        test = Base.from_json_string('[{"id": 89}]')
        self.assertIs(type(test), list)

if __name__ == "__main__":
    unittest.main()
