#!/usr/bin/python3
"""Object to text file using JSON."""
import json


def save_to_json_file(my_obj, filename):
     """Write an object to a text file using JSON rep."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
