#!/usr/bin/python3
class BaseGeometry:
    """
    A base class representing base geometry.
    This class can be used as a base class for geometry-related classes.
    """
    def area(self):
        """
        Raises an Exception indicating that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the given value.
        Args:
        name (str): The name of the value being validated.

        value:
        The value to be validatd.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

        class Rectangle(BaseGeometry):
            """
            A class representing a rectangle.
            Inherits from the BaseGeometry class.
            Public instance attributes:
            width(int): The width of the rectangle.
            height(int): The height of the rectangle.
            """

        def __init__(self, width, height):
            """
            Initializes a Rectangle instance with the given width and height.
            Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            """
            super().__init__()
            self.__width = width
            self.integer_validator("width", width)
            self.__height = height
            self.integer_validator("height", height)

        def area(self):
            """
            Calculates and returns the area of the rectangle.
            Returns:
                int: The area of the rectangle (widht * height).
            """
            return self.__width * self.__height

        def __str__(self):
            """
            Returns a string representation of the Rectangle instance.

            Returns:
                str: A string containing information about the width and height of the rectangle.
            """
            return f"[Rectangle] {self.__width}/{self.__height)"
