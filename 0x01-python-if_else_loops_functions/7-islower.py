#!/usr/bin/python3
# File: 7-islower.py
# Auth: Musa_kalamz A Ogunsolu

""" checks for lowercase character """

def islower(c):
    """Function checks for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
