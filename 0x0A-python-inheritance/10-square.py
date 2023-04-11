#!/usr/bin/python3
"""
this class is used to compute area of a square based on rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this class inherits  from rectangle
    """
    def __init__(self, size):
        """
        instantiation
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
