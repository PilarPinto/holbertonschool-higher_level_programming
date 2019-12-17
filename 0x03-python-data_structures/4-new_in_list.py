#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    c_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return c_list
    c_list[idx] = element
    return c_list
