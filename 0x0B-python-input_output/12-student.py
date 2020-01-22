#!/usr/bin/python3
""" 12. Student to JSON with filter """


class Student:
    """ Creating a class called Student that defines a student. """

    def __init__(self, first_name, last_name, age):
        """ Using __init__ method.
        Args:
            first_name: public instance attribute
            last_name: public instance attribute
            age: public instance attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Creating a public instance method.
        Note:
            Retrieves a dict representation of a Student instance.
        Args:
            attrs: given attributes
        Returns:
            If attrs is a list of strings, only attribute names
            contained in the list.
            Otherwise, all attributes should be retrieved.
        """
        if isinstance(attrs, list) and \
                all(isinstance(element, str) for element in attrs):
            return self.__dict__
