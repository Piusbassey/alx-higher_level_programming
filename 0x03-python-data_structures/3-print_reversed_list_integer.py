#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    """
    Prints all integers of a list in reverse.
    Args:
    my_list(list): The list of integers to be printed in reverse.
    """
    if len(my_list) == 0:
        return
    print("{:d}".format(my_list[-1]))
    print_reversed_list_integer(my_list[:-1])

 my_list = [1, 2, 3, 4, 5]
 print_reversed_list_integer(my_list)
