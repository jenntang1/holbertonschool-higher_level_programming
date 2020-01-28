#!/usr/bin/python3
""" 1. Base class """
import json


class Base:
    """ Creating a base class.
    Note:
        This will manage the id attribute in all other
        classes and avoid duplicating the same code.
    Attributes:
        __nb_objects: private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Using __init__ method.
        Note:
            If id is not None, assign id.
            If id is None, increment __nb_objects and
            assign new value to id.
        Args:
            id: public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Creating JSON string representation static method.
        Args:
            list_dictionaries: list of dictionaries
        Returns:
            If None or empty, return "[]"
            If not None or empty, return JSON str rep
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Creating JSON save to file class method.
        Note:
            If None or empty, save to an empty list
            If not None or empty, save to JSON file
        Args:
            cls: class Base
            list_objs: list of instances inherited from Base
        """
        if list_objs is None:
            list_objs = []
        else:
            my_list = []
            for objs in list_objs:
                my_list.append(objs.to_dictionary())
            with open("{}.json".format(cls.__name__), 'r+') as file_obj:
                file_obj.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """ Creating JSON string from dictionary static method.
        Args:
            json_string: string representing a list of dictionaries
        Returns:
            If None or empty, return empty list
            If not None or empty, return the list
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
