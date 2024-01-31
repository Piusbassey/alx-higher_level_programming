#!/usr/bin/python3
def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Examples:
        >>> print_square(4)
        ####
        #  #
        #  #
        ####
        >>> print_square(1)
        #
        >>> print_square(0)

        >>> print_square(-1)
        Traceback (most recent call last):
            ...
        ValueError: size must be >= 0
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # Check if size is positive
    if size < 0:
        raise ValueError("size must be >= 0")
    # Print the square
    for i in range(size):
        # Print the first and last line with full #
        if i == 0 or i == size - 1:
            print("#" * size)
        # Print the inner lines with # and spaces
    else:
        print("#" + " " * (size - 2) + "#")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
