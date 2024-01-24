#!/usr/bin/python3
"""
Module containing a class MagicClass that does the same as the given Python bytecode.
"""
import math


class MagicClass:
    """
    A class representing MagicClass.

    Attributes:
        __radius (float): The radius value.
    """

    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance.

        Args:
            radius (float or int, optional): The radius value.
                Defaults to 0.
        Raises:
            TypeError: If radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

