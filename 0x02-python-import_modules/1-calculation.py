#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1 as operators
    a = 10
    b = 5
    print('{} + {} = {}'.format(a, b, operators.add(a, b)))
    print('{} - {} = {}'.format(a, b, operators.sub(a, b)))
    print('{} * {} = {}'.format(a, b, operators.mul(a, b)))
    print('{} / {} = {}'.format(a, b, operators.div(a, b)))
