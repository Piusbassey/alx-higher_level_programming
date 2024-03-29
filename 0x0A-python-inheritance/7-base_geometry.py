#!/usr/bin/python3
class BaseGeometry:
    """
    A base class representing base geometry.

    This class can be used as a base class for geometry-related classes.
    """

    def area(self):
        """
        Raises an Exception indicating that the area() method is not implemented.

        Raises:
            Exception: Indicating that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the given value.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
