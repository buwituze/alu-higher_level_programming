#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary with the same keys
    multiplied_dictionary = {key: value * 2 for key, value in a_dictionary.items()}

    return multiplied_dictionary
