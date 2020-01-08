#!/usr/bin/python3
def weight_average(my_list=[]):
    numerator = 0
    add_sec = 0
    average = 0
    if my_list:
        for tup in my_list:
            numerator += (tup[0] * tup[1])
            add_sec += tup[1]
            average = numerator / add_sec
        return average
    return 0
