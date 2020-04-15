#!/usr/bin/python3
'''The function to fetches https://intranet.hbtn.io/status'''
import requests

if __name__ == "__main__":
    va = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(str(va))))
    print('\t- content: {}'.format(va.text))
    va.close()
