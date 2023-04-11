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


"""
This is the inheritence of base geometery
"""


class Rectangle(BaseGeometry):
    """
    this is used to validate and calculate area
    """
    def __init__(self, width, height):
        """
        instantation
        Args: width: width of the rectangle
        height: heigt of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        This method calculates area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        The str function
        """
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


"""
this class is used to compute area of a square based on rectangle
"""


class Square(Rectangle):
    """
    inherits from the base Rectangle
    """
    def __init__(self, size):
        """
        instantiation
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        area of square
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        str of square
        """
        return("[Square] {:d}/{:d}".format(self.__size, self.__size))
