#!/usr/bin/python3
"""
this method returns lists of methods and attributes in the object
"""


def lookup(obj):
    """
    Returns the list of methods and attributes
    Args:
        obj: is the object to be evaluated
        """
    return dir(obj)
