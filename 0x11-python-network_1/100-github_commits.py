#!/usr/bin/python3
'''Get the 10 first commits'''
import requests
import sys

if __name__ == "__main__":

    var = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1]))
    filej = var.json()

    for ind in filej[:10]:
        sha = ind.get('sha')
        authors = ind.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, authors))
