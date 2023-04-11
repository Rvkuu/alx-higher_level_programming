#!/usr/bin/python3
"""
This is used to print a subclass
Return: True or False
"""


def inherits_from(obj, a_class):
    """
    a method used to return true if it is a subclass
    Args:
        obj: is a class objected to be tasted
        a_class: is the type
        Return: True or False
        """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return (True)
    else:
        return (False)
