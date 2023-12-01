#!/bin/use/python3
""" class to define square"""


class Square:
    """
    Representation of a square.
    """
    def __init__(self, size=0):
        """
        the init function that gets invoked when a new instance is created
        :param size:
        """
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

        except Exception as e:
            raise e

