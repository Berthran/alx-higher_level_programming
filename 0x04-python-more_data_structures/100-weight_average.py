#!/usr/bin/python3

def weight_average(my_list=[]):
    ''' Returns a weighted average of all integer tuples '''
    if len(my_list) == 0:
        return (0)
    total_score = 0
    total_weight = 0
    for tup in my_list:
        tup_prod = 1
        for num in tup:
            tup_prod *= num
        total_score += tup_prod
        total_weight += num
    return (total_score/total_weight)
