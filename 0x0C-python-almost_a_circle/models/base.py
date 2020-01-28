#!/usr/bin/python3
"""
1. Base class
15. Dictionary to JSON string
16. JSON string to file
17. JSON string to dictionary
18. Dictionary to Instance
19. File to instances
"""
import json
from os import path


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
            cls: Rectangle or Square
            list_objs: list of instances inherited from Base
        """
        my_list = []
        if list_objs is not None:
            for objs in list_objs:
                my_list.append(objs.to_dictionary())
        with open("{}.json".format(cls.__name__), 'w') as file_obj:
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

    @classmethod
    def create(cls, **dictionary):
        """ Creating a dummy instance class method.
        Note:
            In order to use the update method,
            the create method must be created first.
        Args:
            cls: Rectangle or Square
            dictionary: kwargs
        Return:
            instance with all attributes already set
        """
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Creating class method.
        Args:
            cls: current class in this method
        Returns:
            If file doesn't exist, return empty list
            If file exists, return list of instances
        """
        new_list = []
        if path.exists("{}.json".format(cls.__name__)):
            with open("{}.json".format(cls.__name__), 'r') as file_obj:
                new_list = cls.from_json_string(file_obj.read())
                instance_list = []
                for dicts in new_list:
                    instance = cls.create(**dicts)
                    instance_list.append(instance)
                return instance_list
        else:
            return []
