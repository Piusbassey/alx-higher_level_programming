#!/usr/bin/python3
def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON
    serialization of an object.
    Args:
        obj: An instance of a class.
    Returns:
        dict: A dictionary description suitable for JSON serialization.
    """
    attributes = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            attributes[key] = value
        return attributes
