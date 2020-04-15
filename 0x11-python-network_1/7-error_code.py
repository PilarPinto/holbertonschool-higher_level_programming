#!/usr/bin/python3
'''
Script that takes in a URL, sends a request to the URL
and displays the body of the response.
'''
import requests
import sys

if __name__ == "__main__":
    var = request.get(sys.arv[1])
    if (int(var.status_code) >= 400):
        print("Error code: {}" .format(var.status_code))
    else:
        print(var.text)
