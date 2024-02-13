#!/usr/bin/python3
"""a script that adds two integers
and returns the output, exeception is raised when
when a the user passes a non int/float value.
"""


def add_integer(a, b=98):
    """
        adds two integers and returns the sum

        parameters:
        -a (int): the first integer
        -b (int): optional, cause it will result to 98

        int: returns sum of two integers.
    """
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    sum = a + b
    return sum
