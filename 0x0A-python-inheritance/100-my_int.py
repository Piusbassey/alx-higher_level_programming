#!/usr/bin/python3
class MyInt(int):
    """
    A class representing a rebel integer.

    Inherits from the int class.
    """
    class MyInt(int):
        def __eq__(self, other):
            # Invert the behavior of ==
        return super().__ne__(other)

    def __ne__(self, other):
        # Invert the behavior of !=
        return super().__eq__(other)

my_i = MyInt(3)
print(my_i)       # Output: 3
print(my_i == 3)  # Output: False
print(my_i != 3)  # Output: True
