#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints all integers of a list horizontally.

    Args:
    my_list: A list of integers.
    """

    for num in my_list:
        print(str.format("{:d}", num))


my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
