#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create an empty list to store True or False values
    result_list = []

    # Iterate through the original list
    for num in my_list:
        # Check if the number is divisible by 2
        result_list.append(num % 2 == 0)

    return result_list
