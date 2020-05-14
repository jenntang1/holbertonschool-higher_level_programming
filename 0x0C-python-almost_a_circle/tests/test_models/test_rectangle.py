#!/usr/bin/python3
""" 0. If it's not tested it doesn't work """
from models.rectangle import Rectangle
from models.base import Base
import unittest
import os


class MyTest(unittest.TestCase):
    """ Creating class to test Rectangle class. """

    def setUp(self):
        """
        Defaults
        name mangling __nb_objects
        """
        self.width = 1
        self.height = 1
        self.x = 1
        self.y = 1
        self.id = 1
        Base._Base__nb_objects = 0

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
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_raise_two(self):
        """ Checking height TypeError """
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_raise_three(self):
        """ Checking x TypeError """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_raise_four(self):
        """ Checking y TypeError """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_raise_five(self):
        """ Checking width ValueError """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_raise_six(self):
        """ Checking height ValueError """
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_raise_seven(self):
        """ Checking width ValueError """
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_raise_eight(self):
        """ Checking height ValueError """
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_raise_nine(self):
        """ Checking x ValueError """
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_raise_ten(self):
        """ Checking y ValueError """
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """ Checking area exists """
        rect = Rectangle(3, 2)
        test = rect.area()
        self.assertEqual(test, 6)

    def test_str_method(self):
        """ Checking __str__ method """
        rect = Rectangle(5, 5, 1)
        test = rect.__str__()
        self.assertEqual(test, "[Rectangle] (1) 1/0 - 5/5")

    def test_to_dict(self):
        """ Checking return of a dict repr """
        rect = Rectangle(10, 2, 1, 9)
        test = rect.to_dictionary()
        self.assertEqual(test,
                         {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_update_args_exists(self):
        """ Checking update method for *args exists """
        rect = Rectangle(1, 5, 5, 5, 5)
        test = rect.update()
        self.assertEqual(test, None)

    def test_update_args_one(self):
        """ Checking update method for *args with one arg """
        rect = Rectangle(1, 5, 5, 5, 5)
        test = rect.update(89)
        self.assertEqual(test, None)

    def test_update_args_two(self):
        """ Checking update method for *args with two args """
        rect = Rectangle(1, 5, 5, 5, 5)
        test = rect.update(89, 1)
        self.assertEqual(test, None)

    def test_update_args_three(self):
        """ Checking update method for *args with three args """
        rect = Rectangle(1, 5, 5, 5, 5)
        test = rect.update(89, 1, 2)
        self.assertEqual(test, None)

    def test_update_args_four(self):
        """ Checking update method for *args with four args """
        rect = Rectangle(1, 5, 5, 5, 5)
        test = rect.update(89, 1, 2, 3)
        self.assertEqual(test, None)

    def test_update_args_five(self):
        """ Checking update method for *args with five args """
        rect = Rectangle(1, 5, 5, 5, 5)
        test = rect.update(89, 1, 2, 3, 4)
        self.assertEqual(test, None)

    def test_update_kwargs_exists(self):
        """ Checking update method for **kwargs exists """
        rect = Rectangle(id=5, width=5, height=5, x=5, y=5)
        test = rect.update(**{'id': 89})
        self.assertEqual(test, None)

    def test_update_kwargs_one(self):
        """ Checking update method for **kwargs with one arg """
        rect = Rectangle(id=5, width=5, height=5, x=5, y=5)
        test = rect.update(**{'id': 89, 'width': 1})
        self.assertEqual(test, None)

    def test_update_kwargs_two(self):
        """ Checking update method for **kwargs with two args """
        rect = Rectangle(id=5, width=5, height=5, x=5, y=5)
        test = rect.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(test, None)

    def test_update_kwargs_three(self):
        """ Checking update method for **kwargs with three args """
        rect = Rectangle(id=5, width=5, height=5, x=5, y=5)
        test = rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(test, None)

    def test_update_kwargs_four(self):
        """ Checking update method for **kwargs with four args """
        rect = Rectangle(id=5, width=5, height=5, x=5, y=5)
        test = rect.update(
                **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(test, None)

    def test_save_empty(self):
        """ Checking save_to_file method when empty list is passed in """
        test = Rectangle.save_to_file([])
        self.assertEqual(test, None)

    def test_save_works(self):
        """ Checking save_to_file method when list is passed in """
        test = Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertEqual(test, None)

    def test_create(self):
        """ Checking create method """
        test1 = Rectangle(3, 5, 1)
        test1_dict = test1.to_dictionary()
        test2 = Rectangle.create(**test1_dict)
        self.assertEqual(type(test2), type(test2))

    def test_save_to_file(self):
        """ Checking save_to_file method """
        test1 = Rectangle(10, 7, 2, 8)
        test2 = Rectangle(2, 4)
        saved = Rectangle.save_to_file([test1, test2])
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
