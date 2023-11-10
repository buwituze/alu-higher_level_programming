#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            # Attempt to print only integers, skip other types
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end=" ")
                count += 1
    except IndexError:
        print("\nError: Index out of range. Printed {} integers.".format(count))
    else:
        print("\nPrinted {} integers.".format(count))
    return count
