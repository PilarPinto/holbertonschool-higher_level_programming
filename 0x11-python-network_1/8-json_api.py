#!/usr/bin/python3
'''The function to request with search API'''
import requests
import sys

if __name__ == "__main__":
    val_q = ""

    if len(sys.argv) == 1:
        val_q = ""
    else:
        val_q = sys.argv[1]

    var = requests.post('http://0.0.0.0:5000/search_user', data={'q': val_q})

    try:
        response = var.json()
        if len(response) == 2:
            print("[{}] {}".format(response['id'], response['name']))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
