#!/usr/bin/python3
def remove_char_at(str, n):
    pre = str[:n]
    post = str[n+1:]
    if n < 0:
        return str
    return pre + post
