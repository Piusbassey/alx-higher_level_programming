#!/usr/bin/python3
def multiple_returns(sentence):

    """
    Returns a tuple with the length of a string and its first character.
    Args:
    sentence: The string to analyze.
    Returns:
    A tuple containing the length of the string.
    """
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])

    sentence = "At school, I learn C!"
    length, first = multjiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
