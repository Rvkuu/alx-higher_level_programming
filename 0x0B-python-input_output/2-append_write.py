#!/usr/bin/python3
"""
This function appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    this method is to add a string to the last line
    Args:
        filename: is a file on which the 'text' string is appended
        text: is the text document to be appended
    """

    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
