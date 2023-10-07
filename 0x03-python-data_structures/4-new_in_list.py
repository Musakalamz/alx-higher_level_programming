#!/usr/bin%python3
# File: 4-new_in_list.py
# Auth: Musa_kalamz A Ogunsolu


def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
       without modifying the original list
    """

    if my_list:
        copy = []
        copy = my_list[:]
        if idx < 0 or idx >= len(my_list):
            return copy
        else:
            copy[idx] = element
            return copy
