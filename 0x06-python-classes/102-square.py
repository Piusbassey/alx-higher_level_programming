#!/usr/bin/python3
"""
Module containing a class Square that defines a square.
"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (float or int, optional): The size of the square.
                Defaults to 0.
        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (float or int): The new size value.
        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison method.

        Args:
            other (Square): The other square to compare.
        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparison method.

        Args:
            other (Square): The other square to compare.
        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Greater than comparison method.

        Args:
            other (Square): The other square to compare.
        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal comparison method.

        Args:
            other (Square): The other square to compare.
        Returns:
            bool: True if the area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Less than comparison method.

        Args:
            other (Square): The other square to compare.
        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal comparison method.

        Args:
            other (Square): The other square to compare.
        Returns:
            bool: True if the area is less or equal, False otherwise.
        """
        return self.area() <= other.area()

