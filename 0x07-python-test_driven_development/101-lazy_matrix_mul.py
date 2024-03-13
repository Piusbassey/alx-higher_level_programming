import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices by using the module NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The product of the matrices.

    Raises:
        TypeError: If m_a or m_b is not a list, a list of lists, or contains non-numerical elements.
        ValueError: If m_a or m_b is empty, or if they can't be multiplied.
    """
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list" if not isinstance(m_a, list) else "m_b must be a list")
    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists" if not all(isinstance(row, list) for row in m_a) else "m_b must be a list of lists")
    # Check if m_a and m_b are not empty
    if not m_a or not m_b or not any(m_a) or not any(m_b):
        raise ValueError("m_a can't be empty" if not m_a or not any(m_a) else "m_b can't be empty")
    # Check if m_a and m_b contain only integers or floats
    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats" if not all(isinstance(num, (int, float)) for row in m_a for num in row) else "m_b should contain only integers or floats")
    # Check if m_a and m_b are rectangles
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size" if not all(len(row) == len(m_a[0]) for row in m_a) else "each row of m_b must be of the same size")
    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    # Convert the lists to numpy arrays
    m_a = np.array(m_a)
    m_b = np.array(m_b)
    # Use the numpy.matmul function to multiply the arrays
    result = np.matmul(m_a, m_b)
    # Return the result array
    return result
