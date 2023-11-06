#!/usr/bin/python3
# File: 1-my_list.py
# Auth: Musa_kalamz A Ogunsolu

"""
This module contains one class: MyList
"""


class MyList(list):
    """
    The class MyList inherits from list
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
