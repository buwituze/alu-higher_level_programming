#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        # Try to format and print the integer value
        print("{:d}".format(value))
        return True
    except ValueError as e:
        # If there's a ValueError, print the error message to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        return False
