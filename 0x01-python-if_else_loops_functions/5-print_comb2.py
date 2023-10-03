#!/usr/bin/python3
# File: 5-print_comb2.py
# Auth: Musa_kalamz A Ogunsolu

""" prints numbers from 0 to 99 """

for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
