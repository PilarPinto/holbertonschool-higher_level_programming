#!/usr/bin/python3
def search_replace(my_list, search, replace):
    tmp_list = []
    for ind in my_list:
        if ind == search:
            tmp_list.append(replace)
        else:
            tmp_list.append(ind)
    return tmp_list
