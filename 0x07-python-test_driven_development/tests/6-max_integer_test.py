#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        """ test for empty list """
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_notlist(self):
        """ test for if not a list """
        my_list = {}
        self.assertEqual(max_integer(my_list), None)

    def test_type(self):
        """ test for type error """
        my_list = ["a", 2, 3]
        self.assertRaises(TypeError, max_integer, my_list)

    def test_unexpected(self):
        """ test for unexpected result """
        my_list = [0x0, -434223]
        self.assertEqual(max_integer(my_list), 0)

    def test_type2(self):
        """ test for type error II """
        my_list = [239487328423, {}]
        self.assertRaises(TypeError, max_integer, my_list)

    def test_maxint(self):
        """ test for max integer in list """
        my_list = [1, 2, 3]
        self.assertEqual(max_integer(my_list), 3)

    def test_dups(self):
        """ test for duplicates in list """
        my_list = [1, 3, 3]
        self.assertEqual(max_integer(my_list), 3)

    def test_single(self):
        """ test for single """
        my_list = [3]
        self.assertEqual(max_integer(my_list), 3)

    def test_negatives(self):
        """ test for negatives """
        my_list = [-3, -4, 5]
        self.assertEqual(max_integer(my_list), 5)

    def test_allnegatives(self):
        """ test for all negatives """
        my_list = [-3, -4, -2345]
        self.assertEqual(max_integer(my_list), -3)

    def test_strings(self):
        """ test for strings """
        my_list = ["Ezra", "Shell"]
        self.assertEqual(max_integer(my_list), "Shell")

    def test_zeros(self):
        """ test for zeros """
        my_list = [0, 0, 0]
        self.assertEqual(max_integer(my_list), 0)

    def test_maxint(self):
        """ test for max int """
        my_list = [9223372036854775807, 9223372036854775807]
        self.assertEqual(max_integer(my_list), 9223372036854775807)

    def test_largeints(self):
        """ test for large ints """
        my_list = [-9223372036854775807, 9223372036854775807]
        self.assertEqual(max_integer(my_list), 9223372036854775807)

    def test_float(self):
        """ test for floats """
        my_list = [4.5, 5, 8.9]
        self.assertEqual(max_integer(my_list), 8.9)

    def test_listnone(self):
        """ test for a list that is None """
        my_list = [None]
        self.assertEqual(max_integer(my_list), None)

    def test_strnone(self):
        """ test for string that is None """
        my_list = "None"
        self.assertEqual(max_integer(my_list), "o")

if __name__ == '__main__':
    unittest.main()
