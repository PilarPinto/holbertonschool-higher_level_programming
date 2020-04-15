#!/usr/bin/python3
'''The function to request and show response body with urllib'''
import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
