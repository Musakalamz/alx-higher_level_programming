#!/usr/bin/python3
# File: 10-divisible_by_2.py
# Auth: ,Musa_kalamz A Ogunsolu


def divisible_by_2(my_list=[]):
    """Fnds all multiples of 2 in a list."""

    multiples = []

    for number in range(len(my_list)):
        if my_list[number] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

        return (multiples)
