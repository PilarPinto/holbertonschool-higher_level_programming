#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    import calculator_1 as opr
    if not (len(argv) == 4):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    nb1 = int(argv[1])
    nb2 = int(argv[3])
    symb = argv[2]

    ops = {'+': opr.add, '-': opr.sub, '*': opr.mul, '/': opr.div}
    for ind in ops:
        if symb == ind:
            print('{} {} {} = {}'.format(nb1, symb, nb2, ops[ind](nb1, nb2)))
            exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
