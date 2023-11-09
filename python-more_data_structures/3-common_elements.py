#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Initialize an empty set to store common elements
    common_set = set()
    # Iterate through elements 
    for elem in set_1:
        # Check if the element is present 
        if elem in set_2:
            # If present, add it to the common set
            common_set.add(elem)
            return common_set
