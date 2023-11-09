#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If a tuple is smaller than 2, use 0 for missing integers
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Add corresponding elements
    result = (a[0] + b[0], a[1] + b[1])

    return result
