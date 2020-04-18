#!/usr/bin/python3
'''The function API twitter'''
import requests
import base64
import sys

if __name__ == "__main__":

    auth_h = "https://api.twitter.com/oauth2/token"
    formc = "{}:{}".format(sys.argv[1], sys.argv[2])
    encrypt_en = base64.b64encode(formc.encode('utf-8'))

    heads = {
        "Authorization": "Basic {}".format(encrypt_en.decode('utf-8')),
        "Content-type": "application/x-www-form-urlencoded;charset=UTF-8"
    }

    data_body = {
        "grant_type": "client_credentials"
    }

    resp = requests.post(auth_h, headers=heads, data=data_body)

    requestAut = {
        "Authorization": "Bearer {}".format(resp.json().get("access_token"))
    }

    match_tweets = "https://api.twitter.com/1.1/search/tweets.json"

    match_heads = {
        "q": sys.argv[3],
        "result_type": recent,
        "count": 5
    }

    match_get = request.get(match_tweets, headers=requestAuth,
                            params=match_heads)

    tweet_posts = match_get.json().get("statuses")

    for ind in tweet_post:
        print("[{}] {} by {}".format(ind.get("id"), ind.get("user"),
                                     ind.get("user"), ind("name")))
