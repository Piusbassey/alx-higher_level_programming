#!/usr/bin/python3
def no_c(my_string):

    """
    Removes all charactes c and C from string.
    Args:
    my_string: The string to remove "c" and "C" from.
    """
    new_string = ""

    for char in my_string:
        if char != "c" and char != 'C':

            new_string += char

    return new_string

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
