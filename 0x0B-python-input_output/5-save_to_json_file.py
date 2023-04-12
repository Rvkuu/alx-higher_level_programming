#!/usr/bin/python3
"""
This is used to save json object to file
"""
from json import dumps


def save_to_json_file(my_obj, filename):
    """
    This will save the object file to file
    Args:
        my_obj: is the object file
        filename: is the filename
    """

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(dumps(my_obj))
