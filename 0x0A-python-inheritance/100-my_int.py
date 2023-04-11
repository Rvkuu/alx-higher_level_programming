#!/usr/bin/python3
"""
This class is used to reverse and override the value of equality
"""


class MyInt(int):
    """
    reverse equality
    """
    def __eq__(self, equality):
        """
        equal to -> not equal to
        """
        return (not super().__eq__(equality))

    def __ne__(self, equality):
        """
        not equalto to-> equal to
        """
        return (not super().__ne__(equality))
