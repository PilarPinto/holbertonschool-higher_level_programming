#!/usr/bin/python3
for number in range(0, 10):
    for number2 in range(0, 10):
        if number < number2:
            if not (number == 8 and number2 == 9):
                print('{}{}, '.format(number, number2), end='')
            else:
                print('{}{}'.format(number, number2), end='')
print('')
