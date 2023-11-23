#!/usr/bin/python3
"""Defining an inherited Func to check for a class."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited is a class.

    Args:
        obj (any): The object to checked.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
