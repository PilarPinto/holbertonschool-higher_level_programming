#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for ind in dir(hidden_4):
        if not ind[:2] == '__':
            print('{}'.format(ind))
