#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replaces an element in the list at a specific position.

    :param my_list: The input list.
    :param idx: The index at which the element should be replaced.
    :param element: The new element to replace at the specified index.
    :return: The original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list


    my_list[idx] = element
    return my_list
