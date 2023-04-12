#!/usr/bin/python3
"""
returns an object represented by a JSON string
"""
from json import loads


def from_json_string(my_str):
    """
    This is used to return json representation
    """
    return (loads(my_str))
