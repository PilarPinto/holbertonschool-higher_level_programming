#!/usr/bin/python3
'''The function sends a request to the URL and
displays the value of the variable X-Request-Id
'''
import requests
import sys

if __name__ == "__main__":
    var = requests.get(sys.argv[1])
    print(var.headers.get('X-Request-Id'))
