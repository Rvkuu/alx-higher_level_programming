#!/usr/bin/python3
"""
This function writes and overrites an string
"""


def write_file(filename="", text=""):
    """
    This method is used to write an string to a file
    it overrites if the file exists
    Args:
        filename: is the file to be edited
        text: is the text to be added to the file
    """

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
