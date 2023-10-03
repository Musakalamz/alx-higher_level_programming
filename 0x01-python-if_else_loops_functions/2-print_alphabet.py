#!/usr/bin/python3
# File: 2-print_alphabet.py
# Auth: Musa_kalamz A Ogunsolu.

""" prints the ASCII alphabet, in lowercase, not followed by a new line. """

for letters in range(97, 123):
    print(f"{chr(letters)}", end="")
