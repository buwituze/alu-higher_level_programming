#!/usr/bin/python3
"""Establishing a Func that reads utf8."""


def read_file(filename=""):
    """Printing the contents of a utf8."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
