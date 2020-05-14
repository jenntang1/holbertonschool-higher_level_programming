#!/usr/bin/python3
""" 0. If it's not tested it doesn't work """
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest
import os


class MyTest(unittest.TestCase):
    """ Creating class to test Square class. """

    def setUp(self):
        """
        Defaults
        name mangling __nb_objects
        """
        self.size = 1
        self.x = 1
        self.y = 1
        self.id = 1
        Base._Base__nb_objects = 0

    def test_all(self):
        """ Checking all attributes """
        test = Square(1, 2, 3, 4)
        self.assertEqual(test.id, 4)

    def test_one(self):
        """ Checking one attributess """
        test = Square(1)
        self.assertEqual(test.size, 1)

    def test_two(self):
        """ Checking two attributes """
        test = Square(1, 2)
        self.assertEqual(test.x, 2)

    def test_three(self):
        """ Checking three attributes """
        test = Square(1, 2, 3)
        self.assertEqual(test.y, 3)

    def test_raise_one(self):
        """ Checking size TypeError """
        with self.assertRaises(TypeError):
            Square("1")

    def test_raise_two(self):
        """ Checking x TypeError """
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_raise_three(self):
        """ Checking y TypeError """
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_raise_four(self):
        """ Checking size ValueError """
        with self.assertRaises(ValueError):
            Square(-1)

    def test_raise_five(self):
        """ Checking x ValueError """
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_raise_six(self):
        """ Checking y ValueError """
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_raise_seven(self):
        """ Checking size ValueError """
        with self.assertRaises(ValueError):
            Square(0)

    def test_str_method(self):
        """ Checking __str__ method """
        sq = Square(3, 1, 3)
        test = sq.__str__()
        self.assertEqual(test, "[Square] (1) 1/3 - 3")

    def test_to_dict(self):
        """ Checking return of a dict repr """
        sq = Square(10, 2, 1)
        test = sq.to_dictionary()
        self.assertEqual(test,
                         {'id': 1, 'size': 10, 'x': 2, 'y': 1})

    def test_update_args_exists(self):
        """ Checking update method for *args exists """
        sq = Square(1, 5, 5, 5)
        test = sq.update()
        self.assertEqual(test, None)

    def test_update_args_one(self):
        """ Checking update method for *args with one arg """
        sq = Square(1, 5, 5, 5)
        test = sq.update(89)
        self.assertEqual(test, None)

    def test_update_args_two(self):
        """ Checking update method for *args with two args """
        sq = Square(1, 5, 5, 5)
        test = sq.update(89, 1)
        self.assertEqual(test, None)

    def test_update_args_three(self):
        """ Checking update method for *args with three args """
        sq = Square(1, 5, 5, 5)
        test = sq.update(89, 1, 2)
        self.assertEqual(test, None)

    def test_update_args_four(self):
        """ Checking update method for *args with four args """
        sq = Square(1, 5, 5, 5)
        test = sq.update(89, 1, 2, 3)
        self.assertEqual(test, None)

    def test_update_kwargs_exists(self):
        """ Checking update method for **kwargs exists """
        sq = Square(id=5, size=5, x=5, y=5)
        test = sq.update(**{'id': 89})
        self.assertEqual(test, None)

    def test_update_kwargs_one(self):
        """ Checking update method for **kwargs with one arg """
        sq = Square(id=5, size=5, x=5, y=5)
        test = sq.update(**{'id': 89, 'size': 1})
        self.assertEqual(test, None)

    def test_update_kwargs_two(self):
        """ Checking update method for **kwargs with two args """
        sq = Square(id=5, size=5, x=5, y=5)
        test = sq.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(test, None)

    def test_update_kwargs_three(self):
        """ Checking update method for **kwargs with three args """
        sq = Square(id=5, size=5, x=5, y=5)
        test = sq.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(test, None)

    def test_save_empty(self):
        """ Checking save_to_file method when empty list is passed in """
        test = Square.save_to_file([])
        self.assertEqual(test, None)

    def test_save_works(self):
        """ Checking save_to_file method when list is passed in """
        test = Square.save_to_file([Square(1)])
        self.assertEqual(test, None)

    def test_create(self):
        """ Checking create method """
        test1 = Square(3, 5, 1)
        test1_dict = test1.to_dictionary()
        test2 = Square.create(**test1_dict)
        self.assertEqual(type(test2), type(test2))

if __name__ == "__main__":
    unittest.main()
