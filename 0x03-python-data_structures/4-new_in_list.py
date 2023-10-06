#!/usr/bin%python3
# File: 4-new_in_list.py
# Auth: Musa_kalamz A Ogunsolu


def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
       without modifying the original lis
    """

    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy = my_list.copy()
    copy[idx] = element
    return (copy)
