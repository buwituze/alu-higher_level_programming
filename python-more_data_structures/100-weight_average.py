#!/usr/bin/python3
def weight_average(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return 0

    #variables to store the sum of prod& the sum of weights
    sum_products = 0
    sum_weights = 0

    #go through the list of tuples
    for score, weight in my_list:
        # Calculate the prodof score& weight, add it to the sum
        sum_products += score * weight
        # Add the weight to the sum of weights
        sum_weights += weight

    #calculate the weighted average
    weighted_avg = sum_products / sum_weights

    return weighted_avg
