#!/usr/bin/python3
"""
creates an object from json file
"""
from json import loads


def load_from_json_file(filename):
    """
    creates an object from a json file
    """
    with open(filename, encoding='utf-8') as file:
        return loads(file.read())
