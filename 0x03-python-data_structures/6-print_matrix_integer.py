#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Args:
    - matrix (list of lists): The matrix to be printed.
    """
    for row in matrix:
        for elem in row:
            print("{:d}".format(elem), end=" ")
        print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print_matrix_integer(matrix)
print("--")
print_matrix_integer()
