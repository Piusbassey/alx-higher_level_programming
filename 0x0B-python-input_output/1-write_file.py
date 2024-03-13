#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number
    of character written.

    Args:
        filename (str): The name of the file to write to.
        Defaults to an empty string.
        text (str): The text to be written to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)

if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
