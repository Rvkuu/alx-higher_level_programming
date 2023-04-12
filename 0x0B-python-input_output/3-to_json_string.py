#!/usr/bin/python3
"""
This is used to return json rep
"""
from json import dumps


def to_json_string(my_obj):
    """
    This returns json rep
    Args:
        my_obj: the file
    """
    return (dumps(my_obj))
