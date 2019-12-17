#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    for number in range(0, len(my_list)):
        if (number == idx):
            my_list[number] = element
            return my_list
