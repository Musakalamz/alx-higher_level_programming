#!/usr/bin/python3
# File: 8-simple_delete.py
# Auth: Musa_kalamz A Ogunsolu


def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary."""
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
