#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for ind in range(x):
        try:
            print("{}".format(int(my_list[ind])), end='')
            count += 1
        except (ValueError, TypeError):
            pass
    print('')
    return count
