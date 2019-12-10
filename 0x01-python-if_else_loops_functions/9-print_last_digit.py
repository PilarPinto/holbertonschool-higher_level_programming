#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        print('{}'.format(number), end='')
        return(number)
    else:
        last_n = abs(number) % 10
        print('{}'.format(last_n), end='')
        return(last_n)
