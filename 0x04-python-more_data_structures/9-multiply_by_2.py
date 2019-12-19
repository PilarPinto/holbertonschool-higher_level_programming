#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    tmp_dict = {}
    for key in a_dictionary:
        tmp_dict[key] = a_dictionary[key] * 2
    return tmp_dict
