#!/usr/bin/python3
'''The function to manage requests API'''
import requests
import sys

if __name__ == "__main__":

    var = requests.get('https://api.github.com/user', auth=(
        sys.argv[1], sys.argv[2]))
    print(var.json().get('id'))
