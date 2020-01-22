#!/usr/bin/python3
""" 11. Student to JSON """


class Student:
    """ Creating a class called Student that defines a student. """

    def __init__(self, first_name, last_name, age):
        """ Using __init__ method.
        Args:
            first_name: public instance attribute
            last_name: public instance attribute
            age: publict instance attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Creating a public instance method.
        Returns:
            A dict representation of a Student instance
        """
        return (self.__dict__)
