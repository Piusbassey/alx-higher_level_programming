#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key (str): The key to be added or updated.
        value (any): The value associated with the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary

if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}

    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print(new_dict)

    print("--")

    print(a_dictionary)

    print("--")
    print("--")

    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print(new_dict)

    print("--")

    print(a_dictionary)

