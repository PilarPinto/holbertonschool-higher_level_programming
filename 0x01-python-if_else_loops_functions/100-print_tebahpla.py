#!/usr/bin/python3
for number in range(90, 64, -1):
    if number % 2 == 0:
        numbers = number + 32
    else:
        numbers = number
    print('{}'.format(chr(numbers)), end='')
