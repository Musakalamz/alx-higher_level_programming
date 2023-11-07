#!/usr/bin/python3
# File: 7-add_item.py
# Auth: Musa_kalamz A Ogunsolu

"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
