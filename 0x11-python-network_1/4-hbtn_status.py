#!/usr/bin/python3
'''The function to fetches https://intranet.hbtn.io/status'''
import requests
import sys

if __name__ == "__main__":
    var = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(str(var))))
    print('\t- content: {}'.format(var.text))
    var.close()
