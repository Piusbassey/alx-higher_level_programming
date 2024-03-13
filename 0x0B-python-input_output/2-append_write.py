#!/usr/bin/python3
def append_write(filename='', text=''):
    """
    Appends a string to the end of a text file (UTF8)
    and returns the number of character added.

    Args:
        filename (str): The name of the file to append to. Defaults to an
        empty string.
        text (str): The text to be appended to the file. Defaults to an 
        empty string.
    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)

if __name__== "__main__":
    nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
