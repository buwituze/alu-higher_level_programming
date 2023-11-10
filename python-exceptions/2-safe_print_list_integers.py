#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                value = my_list[i]
                print("{:d}".format(value), end="")
                count += 1
            except (ValueError, TypeError):
                pass  # Skip non-integer values
    except IndexError:
        pass  # to handle the IndexError when x > list.l
    finally:
        print() 
    return count
