#!/usr/bin/python3
"""Defining a Func to write a file."""


def write_file(filename="", text=""):
    """Write a string to a utf8 text file.

    Args:
        filename: The name of the file to write.
        text: The text to write to the file.
    Returns:
        The nr of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
