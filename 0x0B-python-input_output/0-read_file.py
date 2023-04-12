#!/usr/bin/python3
"""
This Function is used to read and print a file
"""


def read_file(filename=""):
    """
    This method is used to read and print a file
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
