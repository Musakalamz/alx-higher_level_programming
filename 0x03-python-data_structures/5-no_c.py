#!/usr/bin/python3
# File: 5-no_c.py
# Auth: Musa_kalamz A Ogunsolu


def no_c(my_string):
    """emoves all characters c and C"""

    copy = [letters for letters in my_string if letters != 'c' and letters != 'C']
    return ("".join(copy))
