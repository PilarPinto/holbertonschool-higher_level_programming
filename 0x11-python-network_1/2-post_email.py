#!/usr/bin/python3
'''The function to post with urllib'''
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
