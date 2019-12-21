#!/usr/bin/python3
def weight_average(my_list=[]):
    weights = 0
    weighted_scores = []
    if my_list:
        for element in my_list:
            weights += element[1]
            weighted_scores.append(element[0] * element[1])
        return sum(weighted_scores) / weights
    else:
        return 0
