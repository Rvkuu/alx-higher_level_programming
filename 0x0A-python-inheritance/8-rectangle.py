#!/usr/bin/python3
"""
this class inherits Base Geometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectangle class that inherits basegeometry
    """
    def __init__(self, width, height):
        """
        instantation
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
