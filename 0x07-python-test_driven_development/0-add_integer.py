#!/usr/bin/python3
def add_integer(a, b=98):
    """
    This function adds two integers.

    Parameters:
    a (int or float): The first integer.
    b (int or float): The second integer (default is 98).

    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If a or b is not an integer or a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
