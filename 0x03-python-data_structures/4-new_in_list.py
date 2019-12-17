#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = my_list.copy()
    if idx < 0:
        return list
    if idx > len(my_list):
        return list
    for number in range(0, len(list)):
        if (number == idx):
            list[number] = element
            return list
