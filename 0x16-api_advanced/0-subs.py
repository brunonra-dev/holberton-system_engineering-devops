#!/usr/bin/python3
'''queries the Reddit API and returns the number of subscribers'''
import requests


def number_of_subscribers(subreddit):
    '''Function'''
    url = 'http://reddit.com/r/{}/about.json'
    header = {'User-agent': 'Prueba:0-subs:v1'}
    res = requests.get(url.format(subreddit), headers=header)
    if res.status_code != 200:
        return 0
    return res.json().get('data', {}).get('subscribers', 0)
