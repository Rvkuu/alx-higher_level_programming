#!/usr/bin/python3
"""
This method is used to inherit list
"""


class MyList(list):
    """
    This is a inherited class and inherits to list
    """
    def print_sorted(self):
        """
        This method is used to reverse the orderof list elements
        """
        print(sorted(self))
