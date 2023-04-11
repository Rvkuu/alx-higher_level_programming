#!/usr/bin/python3
"""
This method is used to identfy the instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    This returns true if it is of the same class otherwise false
    Args:
       obj: is the object to be tested
       a_class: the class
    """
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
