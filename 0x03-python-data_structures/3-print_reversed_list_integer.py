#!/usr/bin/python3
# File: 3-print_reversed_list_integer.py
# Auth: Musa_kalamz A Ogunsolu


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""

    if isinstance(my_list, list):
        my_list.reverse()
        for index in my_list:
            print("{:d}".format(index))
