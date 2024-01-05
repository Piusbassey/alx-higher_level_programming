#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element list like in C.

    Args:
    my_list: The list to access.
    idx: The index of the element to retrieve.

    Returns:
    None if idx is -ve or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
