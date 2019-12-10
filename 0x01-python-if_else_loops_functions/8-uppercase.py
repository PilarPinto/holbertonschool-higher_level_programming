#!/usr/bin/python3
def uppercase(str):
    word = ''
    for ind in range(len(str)):
        if ord(str[ind]) > 96 and ord(str[ind]) < 123:
            word += chr(ord(str[ind])-32)
        elif ord(str[ind]) > 64 and ord(str[ind]) < 91:
            word += chr(ord(str[ind]))
        else:
            word += chr(ord(str[ind]))
    print('{}'.format(word))
