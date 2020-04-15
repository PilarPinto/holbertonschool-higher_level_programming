#!/usr/bin/python3
'''The function to fetches https://intranet.hbtn.io/status'''
import requests
import sys

if __name__=="__main__":
    x = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(str(x))))
    print('\t- type: {}'.format(x.text))
    x.close()
