#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quonam modo?")
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.

        Quonam modo?


        >>> text_indentation("Non autem hoc: igitur ne illud quidem.")
        Non autem hoc:

        igitur ne illud quidem.

    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Loop through each character in text
    for char in text:
        # Print the character
        print(char, end="")
        # If the character is ., ? or :
        if char in ".?:":
            # Print 2 new lines
            print("\n\n")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
