#!/usr/bin/python3
import math


class MagicClass:
    """ Creating function that finds the area and circumference
        Area = pi * r ** 2 and Circumference = 2 * pi * r
    """
    def __init__(self, radius=0):
        self.radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ Area of circle """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Circumference of circle """
        return (2 * math.pi) * self.__radius
