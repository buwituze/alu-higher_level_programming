#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is within the valid range
    if 0 <= idx < len(my_list):
        # Use list slicing to create a new list excluding the element at idx
        my_list = my_list[:idx] + my_list[idx + 1:]

    return my_list
