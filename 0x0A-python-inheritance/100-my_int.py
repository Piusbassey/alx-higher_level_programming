#!/usr/bin/python3
class MyInt(int):
    """
    A class representing a rebel integer.
    Inherits from the int class.
    """
    def __eq__(self, other):
        """
        Overrides the equality operator (==) to return True if the values
        are not equal.
        Args:
            other: The value to compare with.
        Returns:
            bool: True if the values are not equal; False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=) to return True
        if the values are equal.
        Args:
            other: The value to compare with.
        Returns:
            bool: True if the values are equal; False otherwise.
        """
        return super().__eq__(other)
