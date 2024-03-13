#!/usr/bin/python3
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_items_to_list_and_save(args):
    """
    Adds command-line argumensts to a Python list and saves it to a file.

    Args:
        args (list): List of command-line arguments.
    """
    try:
        try:
            items = load_from_json_file("add_items.json")
        except FileNotFoundError:
            items = []

            items.extend(args)

            save_to_json_file(items, "add_item.json")
        except Exception as e:
            print("Error:", e)

    if __name__== "__main__":
        arguments = sys.argv[1:]
        add_items_to_list_and_save(arguments)
