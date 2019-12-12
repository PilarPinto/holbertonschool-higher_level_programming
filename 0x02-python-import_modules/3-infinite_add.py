#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    add = 0
    for ind in argv[1:]:
        add = add + int(ind)
    print(add)
