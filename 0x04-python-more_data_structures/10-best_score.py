#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        dict: A new dictionary with values multiplied by 2.
    """
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    
    return new_dict

if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}

    new_dict = multiply_by_2(a_dictionary)
    print(new_dict)
    print("--")
    print(a_dictionary)
