#!/usr/bin/python3
python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)'
def add_integer(a, b=98):
    """
    Adds two numbers and returns an integer
    """
    if not (isinstance(a, int, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
