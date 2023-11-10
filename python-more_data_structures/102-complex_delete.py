#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # create a list to store keys that need to be deleted
    keys_to_delete = []

    # Iterate through the dictionary items
    for key, val in a_dictionary.items():
        # check if the value matches the specified value
        if val == value:
            # if a match is found, add the key to the list of keys to delete
            keys_to_delete.append(key)

    # delete the keys with the specified value
    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
