#!/usr/bin/python3
"""
This is the base class
"""


class BaseGeometry:
    """
    This class is used only to pass
    """
    def area(self):
        """
        raises excption
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This is used to raise errors
        Args: name: is the string
            value: is the value to be chacked
        """

        if not isinstance(value, int):
            raise TypeError(f"{name:s} must be an integer")
        if value <= 0:
            raise ValueError(f"{name:s} must be greater than 0")
