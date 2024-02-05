#!/usr/bin/python3
class BaseGeometry:
    """
    A base class representing base geometry.
    This class can be used as a base class for geometry-related
    classes.
    """
    def area(self):
        """
        Raises an Exception indicating that the area() method
        is not implemented.
        Raises:
        Exception: Indicating that the area() method
        is not implemented.
        """
        raise Exception("area() is not implemented")
