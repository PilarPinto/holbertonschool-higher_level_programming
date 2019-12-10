#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_n = abs(number) % 10
else:
    last_n = (abs(number) % 10) * -1
print('Last digit of {} is {} '.format(number, last_n), end='')
if last_n > 5:
    print('and is greater than 5')
elif last_n < 6 and last_n != 0:
    print('and is less than 6 and not 0')
else:
    print('and is 0')
