#!/usr/bin/python3
def weight_average(my_list=[]):
    # check if the list is empty
    if not my_list:
        return 0
    
    # initialize variables to store the sum of products and the sum of weights
    sum_products = 0
    sum_weights = 0
    
    # iterate through the list of tuples
    for score, weight in my_list:
        # calculate the product of score and weight and add it to the sum
        sum_products += score * weight
        # add the weight to the sum of weights
        sum_weights += weight
    
    # calculate the weighted average
    weighted_avg = sum_products / sum_weights
    
    return weighted_avg
